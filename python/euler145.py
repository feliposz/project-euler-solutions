"""Problem 145
16 March 2007

Some positive integers n have the property that the sum [ n +
reverse(n) ] consists entirely of odd (decimal) digits. For instance,
36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers
reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are
not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10**9)?

This is very slow. Check euler145.c (runs in 233 seconds)

This one finished in more than 1 hour. =/
"""

from eulerlib import reverseNum

# Added to eulerlib! 
def isReversible(n):
    """Returns true if a number is reversible.

    A number is reversible if the sum of n + reverseNum(n) produces a
    number with only odd digits.
    """    
    if n % 10 == 0:
        return False
    s = n + reverseNum(n)
    while s > 0:
        digit = s % 10
        if not digit in [1,3,5,7,9]:
            return False
        s //= 10
    return True

count = 0
for n in range(1, 1000000000):
    if isReversible(n):
        count += 1
print(count)
