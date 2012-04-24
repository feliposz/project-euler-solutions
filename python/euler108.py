"""Problem 108
04 November 2005

In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:

1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8 = 1/4

What is the least value of n for which the number of distinct
solutions exceeds one-thousand?

NOTE: This problem is an easier version of problem 110; it is strongly
advised that you solve this one first.
"""

# kind of slow, but gives the right answer
# I need to find some "pattern" to improve this

MAX_SOLUTIONS = 1000

n = 30
# starting from 60 the highest values are always divisible by...
increment = 30

highest = 0
while True:
    x = n + 1
    count = 0
    while count < MAX_SOLUTIONS and x <= n*2:
        if (n * x) % (x - n) == 0:
            count += 1
        x += 1
    if count > highest:
        print(n, count, increment)
        highest = count
    if count >= MAX_SOLUTIONS:
        print(n)
        break
    n += increment

"""
x != 0
y != 0
n != 0

1/x + 1/y = 1/n
1/x = 1/n - 1/y

 n*y     x*y     x*n
----- = ----- - ------
x*n*y   x*n*y   x*n*y

n*y = x*y - x*n

n*y = x*(y - n)
n*y/(y-n) = x

x = n*y/(y-n)
"""
