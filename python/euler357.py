"""Prime generating integers
Problem 357
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""

from eulerlib import timedRun, generatePrimesSieve
from math import sqrt

#LIMIT = 10000
LIMIT = 100000000

print("Generating primes... ", end="")
primes, isPrime = generatePrimesSieve(LIMIT+2)
print("done.")

def isPrimeGeneratingInteger(n):
    if n > 10 and not n%10 in (0, 2, 8):
        return False
    for d in range(1, int(sqrt(n))+1):
        if n % d != 0:
            continue
        nd = n // d
        if d > nd:
            break
        x = d + n // d
        #print(d, "+", n, "/", d, "=", d, "+", n // d, "=",x)
        if not isPrime[x]:
            return False
    return True

total = 0
for i in range(1, LIMIT+1):
    if isPrimeGeneratingInteger(i):
        print(i)
        total += i
print("solution:", total)
