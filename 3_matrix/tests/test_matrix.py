from matrix.matrix import Matrix


def test_eq():
    mx1 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    mx2 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    mx3 = Matrix([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ])

    assert mx1 == mx2
    assert mx2 == mx1
    assert mx1 != mx3
    assert mx3 != mx2


def test_str():
    mx = Matrix([
        [1, 2, 3],
        [4, "hello!", 6],
        [7, 8, 9],
    ])

    assert str(mx) == (
        "Matrix([\n" +
        "\t[1,\t2,\t3],\n" +
        "\t[4,\thello!,\t6],\n" +
        "\t[7,\t8,\t9],\n" +
        "])"
    )


def test_add():
    mx1 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    mx2 = Matrix([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ])

    sum = mx1 + mx2

    assert sum == Matrix([
        [10, 10, 10],
        [10, 10, 10],
        [10, 10, 10],
    ])


def test_mul():
    mx1 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])
    mx2 = Matrix([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ])

    mul = mx1 * mx2

    assert mul == Matrix([
        [9, 16, 21],
        [24, 25, 24],
        [21, 16, 9],
    ])


def test_matmul():
    mx1 = Matrix([
        [1, 2],
    ])
    mx2 = Matrix([
        [9, 8],
        [6, 5],
    ])

    mul = mx1 @ mx2

    assert mul == Matrix([
        [21, 18],
    ])
