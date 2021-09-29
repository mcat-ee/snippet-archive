
import os
from pathlib import Path
import re
import shutil
from datetime import datetime as dt


dir_creation_already_checked = dict()


def get_file_list(path, cutoff, print_total=False):
    pathlist = Path(path).glob('**/*.json')
    relevant_set = list()
    if print_total == True:
        print(f"Total files in directory: {len(pathlist)}")

    for path in pathlist:
        m_time = os.path.getmtime(str(path))
        if m_time < cutoff:
            relevant_set.append(path)
    return relevant_set


def mkdir(path):  # Create directory if not already present
    try:    
        os.mkdir(path)
        print(f"[.]\tMade directory '{path}'")
        dir_creation_already_checked[path] = True

    except FileExistsError:
        if path not in dir_creation_already_checked:
            print(f"[!]\t\tDirectory '{path}' already exists!")
            dir_creation_already_checked[path] = True


def move_file_set(file_paths,  destination_dir):  # Move a set of files to the destination dir
    mkdir(destination_dir)
    total = len(file_paths)
    milestone = 75000
    counter = 0
    for path in file_paths:
        str_path = str(path)
        exposure_site = get_site(str_path)
        file_name = get_file_name(str_path)
        mkdir(destination_dir+"\\"+exposure_site)       # TODO: use path library for this and other paths in script
        shutil.move(path, destination_dir+'\\'+exposure_site + "\\" + file_name)  # noqa
        counter += 1
        if (counter % milestone) == 0:
            print(f"Moved {counter}/{total}")
    print(f"Moved {counter}/{total}")


def get_file_name(file_path):       # Extract the Exposure filename from filename
    pattern = "(Exposure[^\.]*\.json)"
    match = re.search(pattern, file_path)
    if match:
        return match.group(1)
    raise Exception(f"Couldn't extract name from '{file_path}' with pattern '{pattern}'")  # noqa


def get_site(file_path):
    pattern = "(Exposure[^ ]*) - "
    match = re.search(pattern, file_path)
    if match:
        return match.group(1)
    raise Exception(f"Couldn't match '{file_path}' with pattern '{pattern}'")


def print_timing(start, end, stage_name):
    total_time = ((end - start).total_seconds())/60
    print(f"{stage_name}\n\t{start} => {end}")
    print(f"\tTotal time taken (m): {total_time}\n")


if __name__ == "__main__":
    process_start = dt.now()
    file_list = get_file_list("20210909", cutoff=1631810580)
    file_scan_end = dt.now()
    print_timing(process_start, file_scan_end, "Dir scan")
    print(f"Identified {len(file_list)} files to move")
    move_file_set(file_list, 'C:\\momessage_archive')

    process_end = dt.now()
    print_timing(file_scan_end, process_end, "Move op.")
    print_timing(process_start, process_end, "Full Process")
