class Matrix:
    def __init__(self, data):
        self._height = len(data)
        self._width = len(data[0])
        if not all(self._width == len(row) for row in data):
            raise ValueError(f"Malformed matrix: {data}")
        self._data = data

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._data == other._data

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        res = "Matrix([\n"
        for row in self._data:
            res += "\t[" + ",\t".join(map(str, row)) + "],\n"
        res += "])"
        return res

    def _validate_class(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError(f"Expected other to be {self.__class__.__name__}")

    def _validate_same_size(self, other):
        self._validate_class(other)
        if self._height != other._height or self._width != other._width:
            raise ValueError("Matrices must have the same dimensions: {self}, {other}")

    def _validate_matmul_size(self, other):
        self._validate_class(other)
        if self._width != other._height:
            raise ValueError("Matrices are incompatible for matmul")

    def __add__(self, other):
        self._validate_same_size(other)
        return self.__class__([
            [self._data[i][j] + other._data[i][j] for j in range(self._width)]
            for i in range(self._height)
        ])

    def __mul__(self, other):
        self._validate_same_size(other)
        return self.__class__([
            [self._data[i][j] * other._data[i][j] for j in range(self._width)]
            for i in range(self._height)
        ])

    def __matmul__(self, other):
        self._validate_matmul_size(other)
        return self.__class__([
            [sum(self._data[i][k] * other._data[k][j] for k in range(self._width))
            for j in range(other._width)]
            for i in range(self._height)
        ])
