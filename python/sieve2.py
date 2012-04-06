#BUGGY!!!!!!!!!!!!!!!!!!!!!!!!!


#http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# CRIVO DE ERASTÓSTENES

##To find all the prime numbers less than or equal to a given integer n
##by Eratosthenes' method:
##Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
##Initially, let p equal 2, the first prime number.
##Starting from p, count up in increments of p and mark each of these
##numbers greater than p itself in the list. These numbers will be
##2p, 3p, 4p, etc.; note that some of them may have already been marked.
##Find the first number greater than p in the list that is not marked.
##If there was no such number, stop. Otherwise, let p now equal this
##number (which is the next prime), and repeat from step 3.
##When the algorithm terminates, all the numbers in the list that are
##not marked are prime.

import time

primes = [2,]
isPrime = {}

# MemoryError for 10^8 =(
# MAX = 100000000
# < 11 seconds for 10^7
#MAX = 10000000
# 1 second for 10^6
MAX = 10000000

start = time.time()
# skip even numbers
for p in range(3, MAX, 2):
    if isPrime.get(p) is None:
        isPrime[p] = True
        primes.append(p)
        sieve = p * p # no need to mark above p^2
        while sieve < MAX:
            isPrime[sieve] = False
            sieve += p*2 # 2* because of skipping even numbers...


#for num in isPrime.keys():
#    if isPrime[num]:
#        primes.append(num)

print(time.time() - start)        
print(len(primes))
print("len(isPrimes)", len(isPrime))
print("len(primes)", len(primes))
print(primes[0], primes[-1], sum(primes))
