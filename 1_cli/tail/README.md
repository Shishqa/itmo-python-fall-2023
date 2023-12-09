# (yet another) tail.py

Acts like an ordinary [tail](https://man7.org/linux/man-pages/man1/tail.1.html)

## Usage

```bash
$ ./tail.py --help
./tail.py - prints last N lines of file

    help: ./tail.py OPTIONS [PATH...]

    if PATH is not provided, reads lines from stdin and prints last 17 lines,
    if there are multiple PATHs, reads file by file and prints last 10 lines of each file.

    OPTIONS:
        --help - print this message

```

### Tail lines from stdin

```bash
$ for x in {0..100}; do echo $x; done | ./tail.py
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
```

### Tail files

```bash
$ for x in {0..100}; do echo $x; done > test.txt
$ ./tail.py test.txt test.txt
==> test.txt <==
91
92
93
94
95
96
97
98
99
100

==> test.txt <==
91
92
93
94
95
96
97
98
99
100
```
