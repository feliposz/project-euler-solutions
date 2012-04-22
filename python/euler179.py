"""Problem 179
26 January 2008

Find the number of integers 1  n  107, for which n and n + 1 have the
same number of positive divisors. For example, 14 has the positive
divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""

# ~ 200 seconds
# Check a version that takes 1/5 of this time at euler179b.py

from eulerlib import generatePrimesSieve, timedRun

LIMIT = 10000000
primes, isPrime = generatePrimesSieve(LIMIT)

# Not sure if this is a great way to factorate
def factorate(num):
    """Return factors for a given number"""
    if num < 2:
        return {}
    factors = {}
    for p in primes:
        while (num % p) == 0:
            num //= p
            factors[p] = factors.get(p, 0) + 1
        if num == 1:
            break
        if isPrime[num]:
            factors[num] = factors.get(num, 0) + 1
            break
    return factors

def countDivisors(num):
    factors = factorate(num)
    count = 1
    for x in factors.values():
        count *= (x + 1)
    return count

def euler179():
    last = 0
    count = 0
    for n in range(1, LIMIT):
        divisors = countDivisors(n)
        if divisors == last:
            #print(n)
            count += 1
        last = divisors
        if n % 100000 == 0:
            print(n, count)
    print(count)

if __name__ == "__main__":
    timedRun(euler179)
