"""Problem 78
10 September 2004

Let p(n) represent the number of different ways in which n coins can
be separated into piles. For example, five coins can separated into
piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

# I successfully found a way to calculate partitions in problem 76, but the
# function is too slow for this case.

# Then I tried to implement the generating function based on this:
# http://en.wikipedia.org/wiki/Partition_%28number_theory%29#Generating_function
# ...with no success.

# Then I "cheated", and got the function p() below at:
# http://stackoverflow.com/questions/3164305/optimizing-a-partition-function

from eulerlib import pentagonalNum

def generalizedPentagonalNum(n):
    if n%2:
        i = (n + 1)/2
    else:
        i = -n/2
    return pentagonalNum(i)

partitions = [1]
def p(n):
    try:
        return partitions[int(n)]
    except IndexError:
        total = 0
        sign = 1
        i = 1
        k = generalizedPentagonalNum(i)
        while n - k >= 0:
            total += sign * p(n - k)
            i += 1
            if i%2: sign *= -1
            k = generalizedPentagonalNum(i)

        partitions.insert(n, total)
        return total

n = 1
while True:
    x = p(n)
    if x % 10000 == 0:
        print(n, x, sep="\t")
        if x % 1000000 == 0:
            break
    n += 1

#10 9
#100 74
#1000 449
#10000 599    
#100000 11224
#1000000 55374

