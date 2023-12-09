#!/bin/python3
import sys


def main():
    if "--help" in sys.argv:
        print_help(sys.argv[0])
        return

    for i, line in enumerate(get_lines()):
        print(f"{i+1: >6d}  {line}", end="")


def print_help(prog_name):
    print(f"""{prog_name} - enumerates lines of file

    help: {prog_name} OPTIONS [PATH...]

    if PATH is not provided, reads lines from stdin,
    if there are multiple PATHs, reads file by file.

    OPTIONS:
        --help - print this message
    """)


def get_lines():
    if len(sys.argv) == 1:
        while line := sys.stdin.readline():
            yield line
    else:
        for path in sys.argv[1:]:
            with open(path, 'r') as fp:
                while line := fp.readline():
                    yield line


if __name__ == "__main__":
    main()
