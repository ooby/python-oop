import os

path = os.path.abspath('./Pneumonia_unmarked')
listdir = os.listdir(path)

scans = []

for item in listdir:
    scan_path = os.path.join(path, item)
    if not '.' in scan_path:
       scans.append(scan_path)

series = []

for scan in scans:
    _series = os.listdir(scan)
    series_path = os.path.join(scan, _series[0])
    if not '.' in series_path:
        series.append(series_path)

inst_paths = []

for series_item in series:
    instances = os.listdir(series_item)
    instances_path = os.path.join(series_item, instances[0])
    if not '.' in instances_path:
        inst_paths.append(instances_path)

files = []

for item in inst_paths:
    insts = os.listdir(item)
    for item2 in insts:
        item2_path = os.path.join(item, item2)
        if item2.endswith('.dcm'):
            files.append(item2_path)

import pydicom

files_data = (
    pydicom.read_file(filename, force=True)
    for filename in files
) # генератор

for item in files_data:
    print(type(item))
