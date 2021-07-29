
# mv file by extension and modified date
`find .   -mtime -8 -name "*.TXT" -maxdepth 1 -exec mv {} test_find/ \;`

- `-maxdepth` indicates the recursive limit
- `-exec` runs the subsequent command for each line, replacing {} with the line and terminating the command with `\;`
