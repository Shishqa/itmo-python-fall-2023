from matrix.np_matrix import NpMatrix


class PolynomialHashMixin(object):
    """
    Полиномиально-хешируемая матрица
    https://codeforces.com/blog/entry/102652
    """

    _U = 311
    _V = 1117
    _MOD = 1e9 + 7

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __hash__(self):
        res = 0
        for i, row in enumerate(self._data):
            for j, item in enumerate(row):
                res += item * (self._U ** i) * (self._V ** j)
                res %= self._MOD
        return res


class HashedMatrix(NpMatrix, PolynomialHashMixin):

    CACHE_KEY = "__cache"
    PREV_HASH_KEY = "__prev_hash"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __matmul__(self, other):
        self_hash = super(PolynomialHashMixin, self).__hash__()
        if not hasattr(self, self.CACHE_KEY):
            setattr(self, self.CACHE_KEY, {})
            setattr(self, self.PREV_HASH_KEY, self_hash)
        elif getattr(self, self.PREV_HASH_KEY) != self_hash:
            # invalidate cache
            setattr(self, self.CACHE_KEY, {})

        cache = getattr(self, self.CACHE_KEY)

        other_hash = super(PolynomialHashMixin, other).__hash__()
        if other_hash in cache:
            return cache[other_hash]

        res = super(NpMatrix, self).__matmul__(other)
        cache[other_hash] = res
        return res

    # def __hash__(self):
    #     return hash(super(PolynomialHashMixin, self))
