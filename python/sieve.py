#http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import time

# This is the fastest version I could create so far...
# I'm using this in eulerlib.py

# 100 million 69 seconds returns 5761455 primes
# 10 million 6.2 seconds returns  664579 primes
# 1 million 0.58 seconds returns   78498 primes

limit = 1000000

isPrime = [None for i in range(limit)]
isPrime[2] = True
start = time.time()
for p in range(3, limit, 2):
    if isPrime[p] is None:
        isPrime[p] = True
        sieve = p * p
        while sieve < limit:
            isPrime[sieve] = False
            sieve += p * 2
print("Time to create prime table = ", time.time() - start)

print("Creating list of primes...")
primes = []

for num in range(limit):
    if isPrime[num]:
        primes.append(num)
    else:
        isPrime[num] = False

print("Total = ", time.time() - start)
print("len(isPrimes)", len(isPrime))
print("len(primes)", len(primes))
print(primes[0], primes[-1], sum(primes))
