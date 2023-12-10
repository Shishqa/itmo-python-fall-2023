import os
import numpy as np

from matrix.matrix import Matrix
from matrix.np_matrix import NpMatrix


def dump(mx, path):
    with open(path, "w") as fp:
        fp.write(str(mx))

def gen_1_and_2(folder, matrix_class):
    np.random.seed(0)

    mx1 = matrix_class(np.random.randint(0, 10, (10, 10)))
    dump(mx1, os.path.join(folder, "A.txt"))

    mx2 = matrix_class(np.random.randint(0, 10, (10, 10)))
    dump(mx2, os.path.join(folder, "B.txt"))

    mx_add = mx1 + mx2
    dump(mx_add, os.path.join(folder, "matrix+.txt"))

    mx_mul = mx1 * mx2
    dump(mx_mul, os.path.join(folder, "matrix*.txt"))

    mx_matmul = mx1 @ mx2
    dump(mx_matmul, os.path.join(folder, "matrix@.txt"))


def main():
    gen_1_and_2("artifacts/3.1", Matrix)
    gen_1_and_2("artifacts/3.2", NpMatrix)


if __name__ == "__main__":
    main()
