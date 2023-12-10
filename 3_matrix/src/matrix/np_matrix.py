import numpy.lib.mixins as np_mixins


class NpMatrix(np_mixins.NDArrayOperatorsMixin):
    def __init__(self, data):
        self._height = len(data)
        self._width = len(data[0])
        if not all(self._width == len(row) for row in data):
            raise ValueError(f"Malformed matrix: {data}")
        self._data = data

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x._data if isinstance(x, NpMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x._data if isinstance(x, NpMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)

    def __str__(self):
        res = "Matrix([\n"
        for row in self._data:
            res += "\t[" + ",\t".join(map(str, row)) + "],\n"
        res += "])"
        return res
