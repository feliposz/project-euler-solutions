"""Counting block combinations I
Problem 114
A row measuring seven units in length has red blocks with a minimum length of
three units placed on it, such that any two red blocks (which are allowed to be
different lengths) are separated by at least one black square. There are exactly
seventeen ways of doing this.

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, in
general it is permitted to mix block sizes. For example, on a row measuring
eight units in length you could use red (3), black (1), and red (4).
"""

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
    count = 0
    if next == 1:
        for i in range(1, rowsize+1):
            if i != 2: #minimal red block is 3
                count += tiles(rowsize - 1, i)
    else:
        #if block is red, place a black block separating the next
        count = tiles(rowsize - next, 1)
    return count

#don't know why i can't use Memoize inside a function, only in global
tiles = Memoize(tiles)
n = 50
count = 0
for i in range(1, n+1):
    if i != 2:
        count += tiles(n, i)
print(count)
