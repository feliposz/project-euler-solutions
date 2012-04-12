"""Problem 73
02 July 2004

Consider the fraction, n/d, where n and d are positive integers. If nd
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d  8 in ascending
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of
reduced proper fractions for d  12,000?

Note: The upper limit has been changed recently.

"""

# Using common floating division instead of Fraction (euler73.py)
# This was 15 times faster in C. Why so much?

from fractions import gcd
import time

LIMIT = 12000
count = 0

start = time.time()
print("Generating proper fractions between 1/3 and 1/2")
for d in range(2, LIMIT + 1):
    for n in range(1, d):
        if gcd(n, d) == 1:
            f = n/d
            if f > 1/3 and f < 1/2:
                count += 1
print("Generating time =", time.time() - start)

print("Count =", count)
