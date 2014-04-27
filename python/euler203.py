"""Squarefree Binomial Coefficients
Problem 203
The binomial coefficients nCk can be arranged in triangular form, Pascal's triangle, like this:

1
1		1
1		2		1
1		3		3		1
1		4		6		4		1
1		5		10		10		5		1
1		6		15		20		15		6		1
1		7		21		35		35		21		7		1
.........
It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n. Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.
"""

from eulerlib import timedRun, generatePrimesSieve

LIMIT = 11243247
#LIMIT = 100
ROWS = 51

print("Generating primes... ", end="")
primes, isPrime = generatePrimesSieve(LIMIT)
print("done.")

# Not sure if this is a great way to factorate
def factorate(num):
    """Returns a map with prime factors for a given number.

    Note: If num < 2 returns an empty map!"""
    if num < 2:
        return {}
    factors = {}
    for p in primes:
        while (num % p) == 0:
            num /= p
            factors[p] = factors.get(p, 0) + 1
        if num == 1:
            break
    return factors

def isSquareFree(n):
    factors = factorate(n)
    for f in factors:
        if factors[f] > 1:
            return False
    return True

def euler203():
    squareFree = {}

    print("Pascal triangle:")
    for rowNum in range(1, ROWS+1):
        row = []
        for i in range(rowNum):
            if i == 0 or i == rowNum - 1:
                row.append(1)
            else:
                row.append(prevRow[i] + prevRow[i-1])
        mid = len(row)//2 + 1
        for i in range(1,len(row)):
            if i == 0:
                continue
            if i > mid:
                break
            if isSquareFree(row[i]):
                squareFree[row[i]] = True
        #print(row)
        prevRow = list(row)

    print("squareFree:", list(squareFree.keys()))
    return sum(list(squareFree.keys()))

print("solution:", euler203())
