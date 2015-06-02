"""Problem 87
21 January 2005

The smallest number expressible as the sum of a prime square, prime
cube, and prime fourth power is 28. In fact, there are exactly four
numbers below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a
prime square, prime cube, and prime fourth power?
"""

from eulerlib import generatePrimesSieve

def euler84():
    """Solves problem 84 from Project Euler."""
    primes, isPrime = generatePrimesSieve(10000)

    LIMIT = 50000000

    numSet = set([])
    num = 0
    for c in primes:
        c4 = c * c * c * c
        if c4 >= LIMIT:
            break
        for b in primes:
            b3 = b * b * b
            if b3 + c4 >= LIMIT:
                break
            for a in primes:
                a2 = a * a
                num = a2 + b3 + c4
                if num >= LIMIT:
                    break
                numSet.add(num)
    print(len(numSet))
