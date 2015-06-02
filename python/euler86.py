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
    return path*path == pathSq

def memoPCheck(fn, w, h, l):
    k = (w,h,l)
    if k in memoP.keys():
        return memoP[k]
    else:
        r = fn(w,h,l)
        memoP[k] = r
        return r

def memoCCheck(fn, k):
    if k in memoC.keys():
        return memoC[k]
    else:
        r = fn(k)
        memoC[k] = r
        return r

# possiveis otimizacoes:
#   eliminar casos com lados iguais (não pode)
#   eliminar casos que nao sao primos (deve memoizar se for o caso)

##def countIntegerCuboids(m):
##    count = 0
##    for w in range(m, 0, -1):
##        for h in range(w, m+1):
##            for l in range(h, m+1):
##                if memoPCheck(isCuboidPathInteger,w, h, l):
##                    count += 1
##    return count

def countIntegerCuboidsR(m):
    if m <= 0:
        return 0
    else:
        count = 0
        w = m
        for h in range(1, w+1):
            for l in range(1, h+1):
                if isCuboidPathInteger(w, h, l):
                    count += 1
        return count + memoCCheck(countIntegerCuboidsR, m - 1)

def firstToExceed(n):
    m = 1
    while True:
        #c = countIntegerCuboids(m)
        c = countIntegerCuboidsR(m)
        #print(m, c)
        if c > n:
            print(m, c)
            return m;
        m += 1


#w = 6
#h = 3
#l = 5

#print(isCuboidPathInteger(w, h, l))
#print(isCuboidPathInteger(1, 1, 1))

#print(countIntegerCuboids(9))

#print(countIntegerCuboids(99))

def euler86(n):
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

firstToExceed(1000000)
