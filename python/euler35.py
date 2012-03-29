##The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
##
##There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
##
##How many circular primes are there below one million?

import math

memo_isPrime = {}

def isPrime(n):
    if memo_isPrime.get(n) is None:
        memo_isPrime[n] = _isPrime(n)
    return memo_isPrime[n]

# described in Project Euler - Problem 7 
# http://projecteuler.net/project/resources/007_c1bfcd3425fd13f6e9abcfad4a222e35/007_overview.pdf
def _isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True  # 2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True  # we have already excluded 4,6 and 8.
    elif n % 3 == 0:
        return False
    else:
        # n rounded to the greatest integer r so that r*r<=n
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f = f + 6
    return True # in all other cases

def rotate(n):
    s = str(n)
    return int(s[-1] + s[:-1])

def isCircularPrime(n):
    r = rotate(n)
    while (r != n):
        if not isPrime(r):
            return False
        r = rotate(r)
    return True      

count = 1 # 2 is prime and circular
print(2, end=" ")

for num in range(3, 1000000, 2):
    if isPrime(num) and isCircularPrime(num):
        print(num, end=" ")
        count += 1
print()

print("Circular primes = ", count)
