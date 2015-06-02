"""Problem 46
20 June 2003

It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2*1²
15 = 7 + 2*2²
21 = 3 + 2*3²
25 = 7 + 2*3²
27 = 19 + 2*2²
33 = 31 + 2*1²

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum
of a prime and twice a square?
"""

from eulerlib import isPrime, timedRun
import math

def euler46():
    """Solve problem 46 from Project Euler."""
    primes = [2,]
    n = 3
    while (True):
        if isPrime(n):
            primes.append(n)
        else:
            isGoldbach = False
            # Try to decompose the number according to formula
            # n = prime + 2x²
            # n - prime = 2x²
            # (n - prime)/2 = x²
            # sqrt((n - prime)/2) = x
            for prime in primes:
                x = math.sqrt((n - prime)/2)
                if x == math.floor(x):
                    # if x is an integer number, n is a valid composite
                    isGoldbach = True
                    break
            if not isGoldbach:
                print("Fails Goldbach =", n)
                break
        n += 2

if __name__ == "__main__":
    timedRun(euler46)
