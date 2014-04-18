#3d room
import math

memoP = {}
memoC = {}
memoC[0] = 0

def shortestCuboidPathSq(w, h, l):
    p1sq = (h+l) * (h+l) + w * w
    p2sq = (w+h) * (w+h) + l * l
    p3sq = (w+l) * (w+l) + h * h
    return min(p1sq, p2sq, p3sq)

def isCuboidPathInteger(w, h, l):
    pathSq = shortestCuboidPathSq(w, h, l)
    path = math.floor(math.sqrt(pathSq))
    # not the best way to check for perfect square, check: http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
    return path*path == pathSq 

def euler86(n):
    count = 0
    w = 1
    while True:
        for h in range(1, w+1):
            for l in range(1, h+1):
                if isCuboidPathInteger(w, h, l):
                    count += 1
                    print(count, w, h, l)
                    if count > n:
                        return n
        w += 1

euler86(1000000)

