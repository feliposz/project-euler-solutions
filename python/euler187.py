from eulerlib import generatePrimesSieve
import pickle

LIMIT = 10**8

print("Generating primes... ", end="")
#primes, isPrime = generatePrimesSieve(LIMIT//2)
primes = pickle.load(open("primes_10e8.p", "rb"))
print("done.")

print(len(primes))

print("Generating semi-primes")
semiPrimes = 0
for i in range(len(primes)):
    if primes[i] * primes[i] >= LIMIT:
        break
    for j in range(i, len(primes)):
        n = primes[i] * primes[j]
        if n < LIMIT:
            semiPrimes += 1
        else:
            break

#print(semiPrimes.keys())
print(semiPrimes)
