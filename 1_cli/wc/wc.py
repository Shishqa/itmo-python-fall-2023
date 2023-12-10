#!/bin/python3
import sys


def main():
    if "--help" in sys.argv:
        print_help(sys.argv[0])
        return

    results = []
    total = []
    pad = 0
    for path, stats in get_wc():
        pad = max(pad, max(len(str(item)) for item in stats))
        results.append((path, stats))

        if not total:
            total = list(stats)
        else:
            for i, stat in enumerate(stats):
                total[i] += stat

    pad = max(pad, max(len(str(item)) for item in total))
    if len(results) > 1:
        results.append(("total", total))

    for path, stats in results:
        stats = list(map(lambda item: str(item).rjust(pad), stats))
        stats = " ".join(stats)
        if path:
            stats += f" {path}"
        print(stats)


def print_help(prog_name):
    print(f"""{prog_name} - number of lines, words, chars for each file

    help: {prog_name} OPTIONS [PATH...]

    if PATH is not provided, reads from stdin,
    if there are multiple PATHs, reads file by file.

    OPTIONS:
        --help - print this message
    """)


def get_stats(fp):
    lines = 0
    words = 0
    chars = 0
    while line := fp.readline():
        lines += 1
        if line:
            words += len(line.split())
        chars += len(line)

    return lines, words, chars


def get_wc():
    if len(sys.argv) == 1:
        yield (None, get_stats(sys.stdin))
    else:
        for path in sys.argv[1:]:
            with open(path, 'r') as fp:
                yield (path, get_stats(fp))


if __name__ == "__main__":
    main()
