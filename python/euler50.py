"""Problem 50
15 August 2003

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to
a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from eulerlib import generatePrimesSieve, timedRun

def euler50():
    """Solve problem 50 from Project Euler.

    First generate a list of all primes below LIMIT. Then check all
    possible subrange sums of the list that result in a number under
    LIMIT and check if the number is a prime. Pick the largest subrange.
    """
    limit = 1000000
    primes, isPrime = generatePrimesSieve(limit)
    longest = 0
    longest_sum = 0
    longest_range = (0, 0)
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            test = sum(primes[i:j])
            size = j - i
            if test >= limit: 
                break # no need to check subsequent subranges
            if isPrime[test] and size > longest:
                longest = size
                longest_sum = test
                longest_range = (i, j)
    print("consecutive primes = ", longest)
    print("num = ", longest_sum)
    print("range = ", longest_range)

if __name__ == "__main__":
    timedRun(euler50)

##Sample run for limit = 10,000,000 (I think this is fast enough!)
##consecutive primes =  1587
##num =  9951191
##range =  (2, 1589)
##
##Run time for execution of euler50
##Using time.time() = 46.25200009346008
##Using time.clock() = 46.260085200000006
