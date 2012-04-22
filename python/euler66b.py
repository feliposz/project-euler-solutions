"""Problem 66
26 March 2004

Consider quadratic Diophantine equations of the form:

x² – Dy² = 1

For example, when D=13, the minimal solution in x is 649² – 13*180² = 1.

It can be assumed that there are no solutions in positive integers
when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain
the following:

3² – 2*2² = 1
2² – 3*1² = 1
9² – 5*4² = 1
5² – 6*2² = 1
8² – 7*3² = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x
is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the
largest value of x is obtained.
"""

import math

# check here for details:
#http://mathworld.wolfram.com/PellEquation.html

LIMIT = 10000000

def isSquare(num):
    assert num >= 0, "Can't calculate the square root of negatives."
    sq = math.sqrt(num)
    return sq == math.floor(sq)

# A slightly modified version for euler66
def continuedFractionAlt(D):

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
                result = a, p, q, middle + 1
                return result # specialized for this problem!
                #return a[:1] + rest[:middle]

    assert n == LIMIT, "Limit reached for " + D

max_x = 0
max_d = 0
for d in range(2, 1000):
    if not isSquare(d):
        a, p, q, r = continuedFractionAlt(d)
        for i in range(len(p)):
            x = p[i]
            y = q[i]
            eq = x*x - d*y*y
            if eq == 1:
                print("%d² - %d * %d² = 1" % (p[i], d, q[i]))
                if x > max_x:
                    max_x = x
                    max_d = d
                break

print(max_x)
print(max_d)
