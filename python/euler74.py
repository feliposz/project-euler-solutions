"""Problem 74
16 July 2004

The number 145 is well known for the property that the sum of the
factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain
of numbers that link back to 169; it turns out that there are only
three such loops that exist:

169  363601  1454  169
871  45361  871
872  45362  872

It is not difficult to prove that EVERY starting number will
eventually get stuck in a loop. For example,

69  363600  1454  169  363601 ( 1454)
78  45360  871  45361 ( 871)
540  145 ( 145)

Starting with 69 produces a chain of five non-repeating terms, but the
longest non-repeating chain with a starting number below one million
is sixty terms.

How many chains, with a starting number below one million, contain
exactly sixty non-repeating terms?
"""

from eulerlib import timedRun
import math

fact = [math.factorial(n) for n in range(10)]

def sumFactDigits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += fact[digit]
        num //= 10
    return total

def sizeChain(num):
    chain = set([num])
    while True:
        num = sumFactDigits(num)
        if num in chain:
            break
        chain.add(num)
    return len(chain)

def euler74():
    count = 0
    for n in range(1, 1000000):
        size = sizeChain(n)
        if size == 60:
            ##print("Produces a chain of 60 elements =", n)
            count += 1
        if size > 60:
            print(p, size)
    print("Count =", count)

if __name__ == "__main__":
    timedRun(euler74)
