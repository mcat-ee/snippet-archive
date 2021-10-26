

from glob import glob
import json
import shutil


filter_path = {}
with open("filters.json") as f:
    filter_path = json.load(f)

# filter_path = {
#     ".pdf": {     # File extension
#         "pdf(": { # Filename prefix to 'match'
#             "destination": "FOLDER NAME TO SORT ELIGIBLE FILES INTO",
#             "matches": [], # Leave empty
#         },
#       ....
#     },
#       ....
#   }


def get_files(extension, directory="."):
    path = directory+"/*"+extension
    filenames = glob(path)
    print(f"[{extension}]\t{len(filenames)} found in {path}")
    return filenames


def strip_string(string_to_strip):
    return ''.join(filter(lambda x: x in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', string_to_strip))  # noqa


def filter_extension(extension):
    filenames = get_files(extension)
    filter_files(extension, filenames)


def filter_files(extension, filenames):
    kept = []
    filtered = []
    filter_set = filter_path[extension]
    for filename in filenames:
        found_matching_filter = False
        bare_filename = strip_string(filename)
        for key in filter_set.keys():
            if bare_filename.startswith(key):
                filter_set[key]["matches"].append(filename)
    for filter_key in filter_set.keys():
        filter_pattern = filter_set[filter_key]
        pending_file_move_count = len(filter_pattern["matches"])
        destination = filter_pattern["destination"]
        if pending_file_move_count > 0:
            print(f"[{extension}]\tMoving {pending_file_move_count} to {destination}")  # noqa
            for filename in filter_pattern["matches"]:
                try:
                    shutil.move(filename, destination + "\\" + filename)  # noqa
                except FileNotFoundError:
                    filename_terms = filename.split("\\")
                    shutil.move(filename, destination + filename_terms[-1])
        else:
            print(f"[{extension}]\tNo files to move for {filter_key} ")


if __name__ == "__main__":
    for key in filter_path.keys():
        filter_extension(key)
        print()
