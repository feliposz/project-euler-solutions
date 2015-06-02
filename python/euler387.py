"""
A Harshad or Niven number is a number that is divisible by the sum of its digits. 
201 is a Harshad number because it is divisible by 3 (the sum of its digits.) 
When we truncate the last digit from 201, we get 20, which is a Harshad number. 
When we truncate the last digit from 20, we get 2, which is also a Harshad number. 
Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a right truncatable Harshad number.

Also: 
201/3=67 which is prime. 
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime. 
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable. 
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.
"""

from eulerlib import sumDigits, isPrime

def isHarshadNumber(n):
    return n % sumDigits(n) == 0

def isRightTruncHarshadNumber(n):
    while n >= 10:
        if isHarshadNumber(n):
            n = n // 10
        else:
            return False
    return True

def isStrongHarshadNumber(n):
    return isPrime(n / sumDigits(n)) and isHarshadNumber(n)
    
def isStrongRightTruncHarshadPrime(n):
    return isPrime(n) and isRightTruncHarshadNumber(n//10)

def euler387():
    pass

if __name__ == '__main__':
    euler387()
