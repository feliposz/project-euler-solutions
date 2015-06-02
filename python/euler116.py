memo = {}

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def memoize2(fn, a, b):
    t = (a, b)
    if t in memo:
        return memo[t]
    else:
        r = fn(a, b)
        memo[t] = r
        return r

def tiles_ORIGINAL(rowsize, color):
    if rowsize < color:
        #can't place a colored tile
        return 0
    if rowsize == color:
        return 1
    else:
        # placed a colored tile in the beginning
        a = 1 + memoize2(tiles, rowsize-color, color)
        # placed no colored tiles in the beginning
        b = memoize2(tiles, rowsize-1, color)
        return a + b

def tiles(rowsize, color):
    if rowsize < color:
        #can't place a colored tile
        return 0
    if rowsize == color:
        return 1
    else:
        # placed a colored tile in the beginning
        a = 1 + tiles(rowsize-color, color)
        # placed no colored tiles in the beginning
        b = tiles(rowsize-1, color)
        return a + b

tiles = Memoize(tiles)
n = 50
print(tiles(n, 2) + tiles(n, 3) + tiles(n, 4))

