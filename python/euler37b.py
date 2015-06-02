##Projece Euler - Problem 37
##
##The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
##
##Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
##
##NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


#generate primes without sieve of eratosthenes

import math
import time

# described in Project Euler - Problem 7 
# http://projecteuler.net/project/resources/007_c1bfcd3425fd13f6e9abcfad4a222e35/007_overview.pdf
def isPrime(n):
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

def isTruncatable(p):
    s = str(p)
    for i in range(1, len(s)+1):
        rightTrunc = int(s[:i])
        leftTrunc = int(s[-i:])
        #print(rightTrunc, leftTrunc)
        if (not isPrime(rightTrunc)):
            return False
        if (not isPrime(leftTrunc)):
            return False
    return True

# < 9 seconds vs. 1 second with sieve of eratosthenes
MAX = 1000000
# check sieve2.py !!!

start = time.time()
#primes = [2,]

total = 0
count = 0

for num in range(3, MAX, 2):
    if isPrime(num):
        if num > 10 and isTruncatable(num):
            print(num)
            count += 1
            total += num
            if count == 11:
                break

print("Total =", total)
        
print(time.time() - start)        


        



