"""Counting block combinations II
Problem 115
NOTE: This is a more difficult version of problem 114.

A row measuring n units in length has red blocks with a minimum length of m
units placed on it, such that any two red blocks (which are allowed to be
different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row
can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which
the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and
F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count
function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first
exceeds one million.
"""

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def tiles(rowsize, next, minimal):
    if rowsize < next:
        return 0
    if rowsize == next:
        return 1
    count = 0
    if next == 1:
        for i in range(1, rowsize+1):
            if i == 1 or i >= minimal:
                count += tiles(rowsize - 1, i, minimal)
    else:
        #if block is red, place a black block separating the next
        count = tiles(rowsize - next, 1, minimal)
    return count

#don't know why i can't use Memoize inside a function, only in global
tiles = Memoize(tiles)
m = 50
#n = 50
for n in range(50, 10000):
    count = 0
    for i in range(1, n+1):
        if i == 1 or i >= m:
            count += tiles(n, i, m)
    print(m, n, count)
    if count > 1000000:
        print("HERE!")
        break
