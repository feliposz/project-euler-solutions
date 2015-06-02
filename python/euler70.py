"""
Problem 70
21 May 2004

Euler's Totient function, φ(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to
n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and
8, are all less than nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive
number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1  n  107, for which φ(n) is a permutation of n
and the ratio n/φ(n) produces a minimum.

"""

import math
from fractions import gcd
from eulerlib import timedRun, generatePrimesSieve

LIMIT = 10000000

#print("Generating primes... ", end="")
#primes, isPrime = generatePrimesSieve(LIMIT)
#print("done.")

# "fast" phi ???
def slow_eulerPhi(n):
    """Calculate phi using euler's product formula."""
    assert math.sqrt(n) <= primes[-1], "Not enough primes to deal with " + n

    # For details, check:
    # http://en.wikipedia.org/wiki/Euler's_totient_function#Euler.27s_product_formula
    prod = n
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            prod *= 1 - (1 / p)
    return int(prod)

# faster for generating individual phis
def eulerPhi(n):
    """Calculate phi(n), where phi is euler's totient function.

    Faster for calculating individual numbers.    
    For a large set, use generateEulerPhiSieve.
    """
    phi = n
    i = 0
    p = primes[0]
    primeCount = len(primes)
    while i < primeCount and p*p <= n:
        p = primes[i]
        if n % p == 0:
            phi = phi - phi // p
            while n % p == 0:
                n //= p
        i += 1
    if n > 1:
        phi = phi - phi // n
    return phi

# Very fast. For details and further optimizations, check: 072_overview.pdf
def generateEulerPhiSieve(limit):
    """Return a list of 'phis' where phis[n] == phi(n)."""
    limit = limit + 1
    phis = list(range(limit))
    # initialise array
    for n in range(2, limit):
        # n is a prime, for all multiples
        # of n multiply with (1-1/n)
        if phis[n] == n:
            for m in range(n, limit, n):
                phis[m] = phis[m] - phis[m] // n
    return phis

import time

start = time.time()
print("Generating euler phi sieve... ", end="")
phis = generateEulerPhiSieve(10000000)
print("done.")
print("Time to generate =", time.time() - start)

def euler70():
    minRatio = 2
    for n in range(2, LIMIT):
        pn = phis[n]
        a = sorted(list(str(n)))
        b = sorted(list(str(pn)))
        if a == b:
            ratio = n/pn
            if ratio < minRatio:
                minRatio = ratio
                print(n, pn, ratio)
                print("minRatio =", minRatio)
    print("Solution =", minRatio)
