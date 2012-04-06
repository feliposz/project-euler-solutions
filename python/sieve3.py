import time

#A simplistic implementation of the Sieve described in
#http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

#Simple, but not very efficient

limit = 1000000

start = time.time()
isPrime = [True for i in range(limit)]
isPrime[0] = False
isPrime[1] = False
for i in range(2, limit//2):
    if isPrime[i]:
        j = 2
        while i * j < limit:
            isPrime[i*j] = False
            j += 1

print("Time to create prime hash = ", time.time() - start)

primes = []

print("Creating list of primes...")
for num in range(limit):
    if isPrime[num]:
        primes.append(num)

print("Total = ", time.time() - start)

print("len(isPrimes)", len(isPrime))
print("len(primes)", len(primes))
print(primes[0], primes[-1], sum(primes))
