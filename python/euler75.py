"""Problem 75
30 July 2004

It turns out that 12 cm is the smallest length of wire that can be
bent to form an integer sided right angle triangle in exactly one way,
but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form
an integer sided right angle triangle, and other lengths allow more
than one solution to be found; for example, using 120 cm it is
possible to form exactly three different integer sided right angle
triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L
1,500,000 can exactly one integer sided right angle triangle be
formed?

Note: This problem has been changed recently, please check that you
are using the right parameters.

"""

import math
from fractions import gcd

# Check this for details on how to calculate pythagorean triples
# http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

LIMIT = 1500000

print("Forming triangles")
perimeters = {}
m = 1
limit_m = math.sqrt(LIMIT) + 1
while m <= limit_m:
    n = 1
    while m > n:
        if gcd(m, n) == 1 and (m - n) % 2 == 1:
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            k = 1
            p = a + b + c
            p2 = p
            while p2 <= LIMIT:
                perimeters[p2] = perimeters.get(p2, 0) + 1
                #print(a*k, b*k, c*k, p2)
                k += 1
                p2 = k * p            
            if p > LIMIT:
                break
        n += 1
    m += 1

print("Checking unique triangles")
count = 0
for p in perimeters:
    if perimeters[p] == 1:
        count += 1
print(count)

