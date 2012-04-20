"""Problem 125
04 August 2006

The palindromic number 595 is interesting because it can be written as
the sum of consecutive squares: 6² + 7² + 8² + 9² + 10² + 11²+ 12².

There are exactly eleven palindromes below one-thousand that can be
written as consecutive square sums, and the sum of these palindromes
is 4164. Note that 1 = 0² + 1² has not been included as this problem
is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both
palindromic and can be written as the sum of consecutive squares.
"""

from eulerlib import isNumPalindrome
import math

SUM_LIMIT = 100000000
LIMIT = int(math.sqrt(SUM_LIMIT))
palindromes = {}
for low in range(1, LIMIT + 1):
    if low*low >= SUM_LIMIT:
        break
    for high in range(low+1, LIMIT+1):
        sum_squares = 0
        for num in range(low, high+1):
            sum_squares += num*num
        if sum_squares >= SUM_LIMIT:
            break
        if isNumPalindrome(sum_squares):
            palindromes[sum_squares] = 1

count = 0
sum_palindromes = 0
for n in palindromes:
    count += 1
    sum_palindromes += n
print(count, sum_palindromes)
