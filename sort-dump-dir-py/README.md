
Please use `download_sorter.py`; `sorter.py` is a legacy implementation.

# Configuration
Create a JSON file labelled `filters.json` using the following format:

```
{
     ".pdf": {     # File extension
         "pdf(": { # Filename prefix to 'match'
             "destination": "FOLDER NAME TO SORT ELIGIBLE FILES INTO",
             "matches": [], # Leave empty
         },
       .... Add more prefixes for .pdf files here
     },
     .... Add more extensions for filtering here
}
```

Each top-level key identifies a file extension to be sorted; the object pointed to by the key encapsulates a set of filename prefixes, and where to sort those prefixes.
The `matches` blank list is used by the script to temporarily store the names of the set of files to be moved. It could be moved into the code rather than being on the filter definition itself - _future work_.

# Running the script

Run `python download_sorter.py` to sort the eligible files in the current working directory.

## Output
The ouput of the script will follow this pattern (note: the block unicode characters mark redacted text)
```
[.xls]  0 found in ./*.xls
[.xls]  No files to move for █████
[.xls]  No files to move for ██████

[.xlsx] 52 found in ./*.xlsx
[.xlsx] No files to move for ████████ ████████ ██████████
[.xlsx] No files to move for ████████ ██████ █████
[.xlsx] No files to move for ████████ ██████ ██████
[.xlsx] No files to move for ████████ ███ ████
```
