import math

# Based on the "simplest" explanation I found at:
# http://mathworld.wolfram.com/PellEquation.html
# check items (7) through (21)

# Even thought every irrational square root has a recurring continued
# fraction representation, I'm limiting their size here just in case...
# This program is not producing anything beyond 218 anyway...

LIMIT = 10000000

def isSquare(num):
    assert num >= 0, "Can't calculate the square root of negatives."
    sq = math.sqrt(num)
    return sq == math.floor(sq)

def continuedFraction(D):

    # n = 0 just for reference
    a = [math.floor(math.sqrt(D))]
    p = [a[0]]
    q = [1]
    P = [0]
    Q = [1]

    assert a[0] * a[0] != D, "D shouldn't be a perfect quare"

    # n = 1 just for reference again
    P.append(a[0])
    Q.append(D - a[0] ** 2)
    a.append(math.floor((a[0] + P[1]) / Q[1]))
    p.append(a[0] * a[1] + 1)
    q.append(a[1])

    # now building the sequence
    n = 2
    while n < LIMIT:
        P.append(a[n-1] * Q[n-1] - P[n-1])
        Q.append((D - P[n] ** 2) / Q[n-1])
        a.append(math.floor((a[0] + P[n]) / Q[n]))
        p.append(a[n] * p[n-1] + p[n-2])
        q.append(a[n] * q[n-1] + q[n-2])
        n += 1

        # TODO: could simplify this a little bit...
        # There is no need for a separate list (rest)
        
        # check for recurring cycle
        rest = a[1:] #exclude first element (always fixed?)
        if rest[-1] == 2 * a[0]:
            middle = len(rest) // 2
            if rest[:middle] == rest[middle:]:
                return a[:1] + rest[:middle]

    assert n == LIMIT, "Limit reached for " + D

odds = 0
evens = 0
max_len = 0
for n in range(1, 10001):
    if not isSquare(n):
        cf = continuedFraction(n)
        if len(cf) > max_len:
            max_len = len(cf)
            #print("max_len =", max_len, "\tn =", n, "\tcf =", cf)
        if (len(cf) - 1) % 2 == 0:
            evens += 1
        else:
            odds += 1
        #print(n, len(cf))
print("Odds %d x %d Evens" % (odds, evens))
print("max_len =", max_len)
