from matrix.matrix import Matrix


class PolynomialHashMixin:
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


class HashedMatrix(Matrix, PolynomialHashMixin):

    CACHE_KEY = "__cache"
    PREV_HASH_KEY = "__prev_hash"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __matmul__(self, other):
        self_hash = hash(self)
        if not hasattr(self, self.CACHE_KEY):
            setattr(self, self.CACHE_KEY, {})
            setattr(self, self.PREV_HASH_KEY, self_hash)
        elif getattr(self, self.PREV_HASH_KEY) != self_hash:
            # invalidate cache
            setattr(self, self.CACHE_KEY, {})

        cache = getattr(self, self.CACHE_KEY)

        other_hash = hash(other)
        if other_hash in cache:
            return cache[other_hash]

        res = super().__matmul__(other)
        cache[other_hash] = res
        return res

    # def __hash__(self):
    #     return hash(super(PolynomialHashMixin, self))
