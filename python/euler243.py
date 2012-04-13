"""Problem 243
02 May 2009
http://projecteuler.net/problem=243

A positive fraction whose numerator is less than its denominator is
called a proper fraction. For any denominator, d, there will be d1
proper fractions; for example, with d  =  12: 1/12 , 2/12 , 3/12 ,
4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient
fraction. Furthermore we shall define the resilience of a denominator,
R(d), to be the ratio of its proper fractions that are resilient; for
example, R(12) = 4/11 . In fact, d  =  12 is the smallest denominator
having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience
R(d) < 15499/94744 .
"""

import math
from fractions import gcd
from eulerlib import timedRun, generatePrimesSieve

LIMIT = 1000000

print("Generating primes... ", end="")
primes, isPrime = generatePrimesSieve(LIMIT)
print("done.")

def slow_phi(num):
    """Calculate phi using a slow method, by checking every relative prime."""
    count = 0
    for den in range(1, num):
        if gcd(num, den) == 1:
            count += 1
    return count

#TODO: incorporate phi and factorate into eulerlib

# "fast" phi ???
def phi(n):
    """Calculate phi using euler's product formula."""
    assert math.sqrt(n) < primes[-1], "Not enough primes to deal with " + n

    # For details, check:
    # http://en.wikipedia.org/wiki/Euler's_totient_function#Euler.27s_product_formula
    prod = n
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            prod *= 1 - (1 / p)
    return int(prod)

# Not sure if this is a great way to factorate
def factorate(num):
    """Returns a map with prime factors for a given number.

    Note: If num < 2 returns an empty map!"""
    if num < 2:
        return {}
    factors = {}
    for p in primes:
        while (num % p) == 0:
            num /= p
            factors[p] = factors.get(p, 0) + 1
        if num == 1:
            break
    return factors

def resilience(d):
    """Returns the ratio of proper fractions for denominator d that
    cannot be cancelled, i.e. that are resilient."""
    
    return phi(d) / (d - 1)


def euler243():
    """Solve problem 243 for Project Euler."""

    expectedResilience = 15499/94744
    
    d = 4
    last = 1.0
    
    i = 0 # index in the prime list
    prod = primes[i] # product of primes to be used as adder
    
    while True:
        r = resilience(d)
        if r < expectedResilience:
            break
        print(d, r, prod)

        # When r(d) > last generated, go back one
        # and compute the next product of primes
        if r > last:
            d -= prod
            i += 1
            prod *= primes[i]
            print("OPS! go back one")
        last = r           
        d += prod

    print(d)
    
def test():
    """Slow solution to problem 243 for Project Euler by testing every
    possible value for d."""

    # Test value... because 15499/94744 will take too long
    expectedResilience = 1/4 #15499/94744    
    d = 2
    last = 1.0   
    while True:
        r = resilience(d)
        if r < expectedResilience:
            break
        if r < last:
            last = r
            print(d, r)
        d += 1

    print(d)

if __name__ == "__main__":
    timedRun(euler243)


