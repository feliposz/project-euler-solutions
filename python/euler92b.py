"""Problem 92
01 April 2005
http://projecteuler.net/problem=92

A number chain is created by continuously adding the square of the
digits in a number to form a new number until it has been seen before.

For example,

44  32  13  10  1  1
85  89  145  42  20  4  16  37  58  89

Therefore any chain that arrives at 1 or 89 will become stuck in an
endless loop. What is most amazing is that EVERY starting number will
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

from eulerlib import timedRun

chainTable = []
sqTable = [i*i for i in range(0, 10)]

def sumDigitSquares(num):
    global sqTable
    sqSum = 0
    while num > 0:
        sqSum += sqTable[num % 10]
        num //= 10
    return sqSum
            
def initChainTable():
    global chainTable
    chainTable = [0,]
    for i in range(1, 1000):
        n = sumDigitSquares(i)
        while n != 1 and n != 89:
            n = sumDigitSquares(n)
        chainTable.append(n)

def chainResult(num):
    global chainTable
    if num >= 1000:
        num = sumDigitSquares(num)
    return chainTable[num]

def euler92():
    """A solution to problem 92 from Project Euler."""
    initChainTable()
    count = 0
    for num in range(1,10000000):
        if chainResult(num) == 89:
            count += 1 
    print(count)

if __name__ == "__main__":
    timedRun(euler92)
