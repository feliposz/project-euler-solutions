class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def tiles(rowsize, next):
    if rowsize < next:
        return 0
    if rowsize == next:
        return 1
    k = tiles(rowsize - next, 1)
    r = tiles(rowsize - next, 2)
    g = tiles(rowsize - next, 3)
    b = tiles(rowsize - next, 4)
    return k + r + g + b


tiles = Memoize(tiles)
n = 50
print(tiles(n,1) + tiles(n,2) + tiles(n,3) + tiles(n,4))
