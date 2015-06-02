"""Problem 57
21 November 2003

It is possible to show that the square root of two can be expressed as
an infinite continued fraction.

 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the
eighth expansion, 1393/985, is the first example where the number of
digits in the numerator exceeds the number of digits in the
denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""

from fractions import Fraction

# Recursion with memoization
_memo = {0: None, 1: Fraction(2, 1)}
def memo_sqrt2den(expansions):
    global _memo
    if _memo.get(expansions) is None:
        _memo[expansions] = Fraction(2, 1) + Fraction(1, memo_sqrt2den(expansions - 1))
    return _memo[expansions]

# Iteration
def sqrt2den(expansions):
    f = Fraction(2, 1)
    while expansions > 1:
        f = Fraction(2, 1) + Fraction(1, f)
        expansions -= 1
    return f

def sqrt2(expansions):
    return Fraction(1, 1) + Fraction(1, memo_sqrt2den(expansions))

def countDigits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

# I implemeted a faster version in Scheme/Racket (euler57.rkt)
# WITHOUT memoization
count = 0
for i in range(1, 1001):
    f = sqrt2(i)
    if countDigits(f.numerator) > countDigits(f.denominator):
        count += 1
print(count)
