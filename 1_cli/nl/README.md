# (yet another) nl.py

Acts like an ordinary [nl](https://man7.org/linux/man-pages/man1/nl.1.html)

## Usage

```bash
$ ./nl.py --help
./nl.py - enumerates lines of file

    help: ./nl.py OPTIONS [PATH...]

    if PATH is not provided, reads lines from stdin,
    if there are multiple PATHs, reads file by file.

    OPTIONS:
        --help - print this message

```

### Enumerate lines from stdin

```bash
$ echo -e 'line1\nline2\nline3\n\nline5' | ./nl.py
     1  line1
     2  line2
     3  line3
     4
     5  line5
```

### Enumerate file

```bash
$ echo -e 'line1\nline2\nline3\n\nline5' > test.txt
$ ./nl.py test.txt
     1  line1
     2  line2
     3  line3
     4
     5  line5
```
