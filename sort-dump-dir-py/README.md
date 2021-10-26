
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

Run `python download_sorter.py` to sort the eligible files in the current working directory.
