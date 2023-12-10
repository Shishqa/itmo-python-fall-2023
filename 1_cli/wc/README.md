# (yet another) wc.py

## Usage

```bash
$ ./wc.py --help
./wc.py - number of lines, words, chars for each file

    help: ./wc.py OPTIONS [PATH...]

    if PATH is not provided, reads from stdin,
    if there are multiple PATHs, reads file by file.

    OPTIONS:
        --help - print this message

```

### Tail lines from stdin

```bash
$ cat README.md | ./wc.py
 40 129 652
```

### Tail files

```bash
$ ./wc.py README.md README.md
  70  129  652 README.md
  70  129  652 README.md
 140  258 1304 total
```
