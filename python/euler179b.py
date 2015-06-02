"""Problem 179
26 January 2008

Find the number of integers 1  n  107, for which n and n + 1 have the
same number of positive divisors. For example, 14 has the positive
divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""

# This is an alternative solution in found in the forum:
# http://projecteuler.net/thread=179

# My (slower) solution is in euler179.py

from eulerlib import timedRun

def euler179b():
    
    LIMIT = 10000000

    sieve = [1 for i in range(LIMIT+1)]
    sieve[0] = 0

    for p in range(2, LIMIT):
        if sieve[p] == 1:
            j = 1
            while j*p < LIMIT:
                count = 2
                test = j
                while test % p == 0:
                    count += 1
                    test //= p
                sieve[j*p] = sieve[j*p] * count
                j += 1
    result = 0
    for i in range(2, LIMIT-1):
        if sieve[i] == sieve[i+1]:
            result += 1
    print(result)

if __name__ == "__main__":
    timedRun(euler179b)
