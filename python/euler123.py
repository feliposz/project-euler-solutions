"""Problem 123
16 June 2006

Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the
remainder when (pn1)^n + (pn+1)^n is divided by (pn)^2.

For example, when n = 3, p3 = 5, and 4³ + 6³ = 280  5 mod 25.

The least value of n for which the remainder first exceeds 109 is
7037.

Find the least value of n for which the remainder first exceeds 1010.
"""

from eulerlib import generatePrimesSieve

primes, isPrime = generatePrimesSieve(1000000)

for n in range(1, len(primes)+1):
    pn = primes[n-1]
    r = ((pn - 1) ** n + (pn + 1) ** n) % (pn * pn)
##    print("%d ^ %d + %d ^ %d = %d ^ 2 (rem: %d)" %
##          (pn - 1, n, pn + 1 , n, pn, r))
    if r > 10**10:
        break

print("n =", n)

print("%d ^ %d + %d ^ %d = %d ^ 2 (rem: %d)" %
      (pn - 1, n, pn + 1 , n, pn, r))
