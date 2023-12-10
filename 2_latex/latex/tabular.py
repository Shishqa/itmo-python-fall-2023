from latex.common import environment


def tabular_row(row):
    return " & ".join(str(item) for item in row) + " \\\\"


def tabular(data):

    data = data or [[]]
    format = " ".join("c" * len(data[0]))

    @environment("tabular", format, indent=1)
    def env():
        rows = map(lambda row: tabular_row(row), data)
        return "\n".join(rows)

    return env
