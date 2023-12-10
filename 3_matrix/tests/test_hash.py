from matrix.hash import HashedMatrix
from matrix.matrix import Matrix


def test_matmul():
    mx1 = HashedMatrix([
        [1, 2],
    ])
    mx2 = HashedMatrix([
        [9, 8],
        [6, 5],
    ])
    res = HashedMatrix([
        [21, 18],
    ])

    mul = mx1 @ mx2
    assert mul == res

    mul = mx1 @ mx2
    assert mul == res

    mul = mx1 @ mx2
    assert mul == res
