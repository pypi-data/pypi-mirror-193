#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0

import os
import struct
import subprocess

# For supporting python 2.6
try:
    subprocess.DEVNULL = subprocess.DEVNULL
except AttributeError:
    subprocess.DEVNULL = open(os.devnull, 'wb')

try:
    subprocess.check_output = subprocess.check_output
except AttributeError:
    def check_output(*popenargs, **kwargs):
        process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
        output, err = process.communicate()
        rc = process.poll()
        if rc:
            raise subprocess.CalledProcessError(rc, popenargs[0])
        return output

    subprocess.check_output = check_output

class DAMONRegion:
    start = None
    end = None
    nr_accesses = None
    age = None

    def __init__(self, start, end, nr_accesses, age):
        self.start = start
        self.end = end
        self.nr_accesses = nr_accesses
        self.age = age

class DAMONSnapshot:
    start_time = None
    end_time = None
    target_id = None
    regions = None

    def __init__(self, start_time, end_time, target_id):
        self.start_time = start_time
        self.end_time = end_time
        self.target_id = target_id
        self.regions = []

class DAMONResult:
    start_time = None
    end_time = None
    nr_snapshots = None
    target_snapshots = None    # {target_id: [snapshot]}

    def __init__(self):
        self.target_snapshots = {}
        self.nr_snapshots = 0

def record_to_damon_result(file_path):
    result = None
    fmt_version = None

    f = open(file_path, 'rb')

    # read record format version
    mark = f.read(16)
    if mark == b'damon_recfmt_ver':
        fmt_version = struct.unpack('i', f.read(4))[0]
    else:
        fmt_version = 0
        f.seek(0)
    result = DAMONResult()

    while True:
        timebin = f.read(16)
        if len(timebin) != 16:
            f.close()
            break
        sec = struct.unpack('l', timebin[0:8])[0]
        nsec = struct.unpack('l', timebin[8:16])[0]
        end_time = sec * 1000000000 + nsec

        nr_tasks = struct.unpack('I', f.read(4))[0]
        for t in range(nr_tasks):
            if fmt_version == 1:
                target_id = struct.unpack('i', f.read(4))[0]
            else:
                target_id = struct.unpack('L', f.read(8))[0]

            if not target_id in result.target_snapshots:
                result.target_snapshots[target_id] = []
            target_snapshots = result.target_snapshots[target_id]
            if len(target_snapshots) == 0:
                start_time = None
            else:
                start_time = target_snapshots[-1].end_time

            snapshot = DAMONSnapshot(start_time, end_time, target_id)
            nr_regions = struct.unpack('I', f.read(4))[0]
            for r in range(nr_regions):
                start_addr = struct.unpack('L', f.read(8))[0]
                end_addr = struct.unpack('L', f.read(8))[0]
                nr_accesses = struct.unpack('I', f.read(4))[0]
                region = DAMONRegion(start_addr, end_addr, nr_accesses, None)
                snapshot.regions.append(region)
            target_snapshots.append(snapshot)

    f.close()

    return result

def perf_script_to_damon_result(script_output):
    result = DAMONResult()
    snapshot = None

    for line in script_output.split('\n'):
        line = line.strip()
        '''
        example line is as below:

        kdamond.0  4452 [000] 82877.315633: damon:damon_aggregated: \
                target_id=18446623435582458880 nr_regions=17 \
                140731667070976-140731668037632: 0 3

        Note that the last field is not in the early version[1].

        [1] https://lore.kernel.org/linux-mm/df8d52f1fb2f353a62ff34dc09fe99e32ca1f63f.1636610337.git.xhao@linux.alibaba.com/
        '''

        fields = line.strip().split()
        if not len(fields) in [9, 10]:
            continue
        if fields[4] != 'damon:damon_aggregated:':
            continue

        start_addr, end_addr = [int(x) for x in fields[7][:-1].split('-')]
        nr_accesses = int(fields[8])
        if len(fields) == 10:
            age = int(fields[9])
        else:
            age = None
        region = DAMONRegion(start_addr, end_addr, nr_accesses, age)

        end_time = int(float(fields[3][:-1]) * 1000000000)
        target_id = int(fields[5].split('=')[1])

        if not target_id in result.target_snapshots:
            result.target_snapshots[target_id] = []
        target_snapshots = result.target_snapshots[target_id]
        if len(target_snapshots) == 0:
            start_time = None
        else:
            start_time = target_snapshots[-1].end_time
        nr_regions = int(fields[6].split('=')[1])

        if snapshot == None:
            snapshot = DAMONSnapshot(start_time, end_time, target_id)
            target_snapshots.append(snapshot)
        snapshot = target_snapshots[-1]
        snapshot.regions.append(region)

        if len(snapshot.regions) == nr_regions:
            snapshot = None

    return result

file_type_record = 'record'             # damo defined binary format
file_type_perf_script = 'perf_script'   # perf script output

def parse_damon_result(result_file):
    script_output = None
    output = subprocess.check_output(
            ['file', '-b', result_file]).decode().strip()
    if output == 'ASCII text':
        with open(result_file, 'r') as f:
            script_output = f.read()
        file_type = file_type_perf_script
    else:
        try:
            script_output = subprocess.check_output(
                    ['perf', 'script', '-i', result_file]).decode()
            file_type = file_type_perf_script
        except:
            file_type = file_type_record

    if file_type == file_type_record:
        result = record_to_damon_result(result_file)
    elif file_type == file_type_perf_script:
        result = perf_script_to_damon_result(script_output)
    else:
        return None, 'unknown result file type: %s (%s)' % (
                file_type, result_file)

    for snapshots in result.target_snapshots.values():
        if len(snapshots) < 2:
            break
        if not result.start_time:
            end_time = snapshots[-1].end_time
            start_time = snapshots[0].end_time
            nr_snapshots = len(snapshots) - 1
            snapshot_time = float(end_time - start_time) / nr_snapshots

            result.start_time = start_time - snapshot_time
            result.end_time = end_time
            result.nr_snapshots = nr_snapshots + 1

        snapshots[0].start_time = snapshots[0].end_time - snapshot_time

        # cut out the fake snapshot for end time
        if len(snapshots) == 2 and len(snapshots[1].regions) == 1:
            region = snapshots[1].regions[0]
            if (region.start == 0 and region.end == 0 and
                    region.nr_accesses == -1 and region.age == -1):
                del snapshots[1]

    return result, None

def write_damon_record(result, file_path, format_version):
    with open(file_path, 'wb') as f:
        f.write(b'damon_recfmt_ver')
        f.write(struct.pack('i', format_version))

        for snapshots in result.target_snapshots.values():
            for snapshot in snapshots:
                f.write(struct.pack('l', snapshot.end_time // 1000000000))
                f.write(struct.pack('l', snapshot.end_time % 1000000000))

                f.write(struct.pack('I', 1))

                if format_version == 1:
                    f.write(struct.pack('i', snapshot.target_id))
                else:
                    f.write(struct.pack('L', snapshot.target_id))

                f.write(struct.pack('I', len(snapshot.regions)))
                for region in snapshot.regions:
                    # skip fake snapshot
                    if region.nr_accesses == -1:
                        continue
                    f.write(struct.pack('L', region.start))
                    f.write(struct.pack('L', region.end))
                    f.write(struct.pack('I', region.nr_accesses))

def write_damon_perf_script(result, file_path):
    '''
    Example of the normal perf script output:

    kdamond.0  4452 [000] 82877.315633: damon:damon_aggregated: \
            target_id=18446623435582458880 nr_regions=17 \
            140731667070976-140731668037632: 0 3
    '''

    with open(file_path, 'w') as f:
        for snapshots in result.target_snapshots.values():
            for snapshot in snapshots:
                for region in snapshot.regions:
                    f.write(' '.join(['kdamond.x', 'xxxx', 'xxxx',
                        '%f:' % (snapshot.end_time / 1000000000.0),
                        'damon:damon_aggregated:',
                        'target_id=%s' % snapshot.target_id,
                        'nr_regions=%d' % len(snapshot.regions),
                        '%d-%d: %d %s' % (region.start, region.end,
                            region.nr_accesses, region.age)]) + '\n')

def write_damon_result(result, file_path, file_type):
    for target_snapshots in result.target_snapshots.values():
        if len(target_snapshots) == 1:
            # we cannot know start/end time of single snapshot from the file
            # to allow it with later read, write a fake snapshot
            snapshot = target_snapshots[0]
            snap_duration = snapshot.end_time - snapshot.start_time
            fake_snapshot = DAMONSnapshot(snapshot.end_time,
                    snapshot.end_time + snap_duration, snapshot.target_id)
            # -1 nr_accesses/ -1 age means fake
            fake_snapshot.regions = [DAMONRegion(0, 0, -1, -1)]
            target_snapshots.append(fake_snapshot)
            result.nr_snapshots += 1
    if file_type == file_type_record:
        write_damon_record(result, file_path, 2)
    elif file_type == file_type_perf_script:
        write_damon_perf_script(result, file_path)
    else:
        print('write unsupported file type: %s' % file_type)

def update_result_file(file_path, file_format):
    result, err = parse_damon_result(file_path)
    if err:
        return err
    write_damon_result(result, file_path, file_format)
    return None

def regions_intersect(r1, r2):
    return not (r1.end <= r2.start or r2.end <= r1.start)

def add_region(regions, region, nr_acc_to_add):
    for r in regions:
        if regions_intersect(r, region):
            if not r in nr_acc_to_add:
                nr_acc_to_add[r] = 0
            nr_acc_to_add[r] = max(nr_acc_to_add[r], region.nr_accesses)

            new_regions = []
            if region.start < r.start:
                new_regions.append(DAMONRegion(
                    region.start, r.start, region.nr_accesses, region.age))
            if r.end < region.end:
                new_regions.append(DAMONRegion(
                        r.end, region.end, region.nr_accesses, region.age))

            for new_r in new_regions:
                add_region(regions, new_r, nr_acc_to_add)
            return
    regions.append(region)

def aggregate_snapshots(snapshots):
    new_regions = []
    for snapshot in snapshots:
        # Suppose the first snapshot has a region 1-10:5, and the second
        # snapshot has two regions, 1-5:2, 5-10: 4.  Aggregated snapshot should
        # be 1-10:9.  That is, we should add maximum nr_accesses of
        # intersecting regions.  nr_acc_to_add contains the information.
        nr_acc_to_add = {}
        for region in snapshot.regions:
            add_region(new_regions, region, nr_acc_to_add)
        for region in nr_acc_to_add:
            region.nr_accesses += nr_acc_to_add[region]

    new_snapshot = DAMONSnapshot(snapshots[0].start_time,
            snapshots[-1].end_time, snapshots[0].target_id)
    new_snapshot.regions = new_regions
    return new_snapshot
