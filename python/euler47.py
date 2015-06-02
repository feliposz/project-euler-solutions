"""Problem 47
04 July 2003

The first two consecutive numbers to have two distinct prime factors
are:

14 = 2  7
15 = 3  5

The first three consecutive numbers to have three distinct prime
factors are:

644 = 2²  7  23
645 = 3  5  43
646 = 2  17  19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from eulerlib import generateNPrimes2, timedRun

primes = []

# Not sure if this is a great way to factorate
def factorate(num):
    """Return factors for a given number"""
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

def countFactors(num):
    count = 0
    div = 2
    while num != 1:
        if num % div == 0:
            count += 1
            while num % div == 0:
                num //= div
        div += 1
    return count

def euler47b():
    """Alternative (slower, but simpler) solution to problem 47 from Project Euler."""
    count = 0
    nfactors = 4
    n = 2
    while True:
        if countFactors(n) == nfactors:
            count += 1
        else:
            count = 0
        if count == nfactors:
            print(n - nfactors + 1)
            break
        n += 1

def euler47a():
    """Solution to problem 47 from Project Euler."""
    global primes
    NPRIMES = 20000 # should probably be much larger for nfactors > 4
    print("Generating", NPRIMES, "...", end="")
    primes = generateNPrimes2(NPRIMES) # should use a better method for much larger numbers...
    print("done.")

    # nfactors = n consecutive numbers to have n distinct factors
    nfactors = 4
    seq = [{} for i in range(nfactors)]
    num = 2
    while num < primes[-1]:
        seq.pop(0) # keep only the last 4
        seq.append(factorate(num))
        hasDistinctFactors = True
        for s in seq:
            if len(s.keys()) != nfactors:
                hasDistinctFactors = False
                break
        if hasDistinctFactors:
            print(num - nfactors + 1, seq[0])
            break
        num += 1

##timedRun(euler47a)
##Generating 20000 ...done.
##134043 {3: 1, 491: 1, 13: 1, 7: 1}
##
##Run time for execution of euler47a
##Using time.time() = 71.26399993896484  \o/ My version rocks!!!!
##Using time.clock() = 71.2725932

##timedRun(euler47b)
##134043
##
##Run time for execution of euler47b
##Using time.time() = 631.2579998970032
##Using time.clock() = 631.2673744
