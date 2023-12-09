#!/bin/python3
import sys


def main():
    if "--help" in sys.argv:
        print_help(sys.argv[0])
        return

    outputs = []
    for path, tail in get_tails():
        output = ""
        if path:
            output += f"==> {path} <==\n"
        output += "".join(tail)
        outputs.append(output)

    print("\n".join(outputs), end="")


def print_help(prog_name):
    print(f"""{prog_name} - prints last N lines of file

    help: {prog_name} OPTIONS [PATH...]

    if PATH is not provided, reads lines from stdin and prints last 17 lines,
    if there are multiple PATHs, reads file by file and prints last 10 lines of each file.

    OPTIONS:
        --help - print this message
    """)


def get_tails():
    if len(sys.argv) == 1:
        lines = sys.stdin.readlines()
        yield (None, lines[-17:])
    else:
        for path in sys.argv[1:]:
            with open(path, 'r') as fp:
                lines = fp.readlines()
                yield (path if len(sys.argv) > 2 else None, lines[-10:])


if __name__ == "__main__":
    main()
