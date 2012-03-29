##145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
##
##Find the sum of all numbers which are equal to the sum of the factorial of their digits.
##
##Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

fact = [math.factorial(num) for num in range(10)]

def sumFactDigits(num):
    tot = 0
    while num > 0:
        tot += fact[num % 10]
        num //= 10
    return tot

total = 0
print("Started...", end="")
for num in range(3, 1000000):
    if num == sumFactDigits(num):
        total += num

print("done.")

print(total)
