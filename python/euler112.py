"""Problem 112
30 December 2005

Working from left-to-right if no digit is exceeded by the digit to its
left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just
over half of the numbers below one-thousand (525) are bouncy. In fact,
the least number for which the proportion of bouncy numbers first
reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the
time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is
exactly 99%.

"""

from eulerlib import timedRun

def isBouncy(num):
    s = str(num)
    increasing = True
    decreasing = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            increasing = False
        if s[i] < s[i + 1]:
            decreasing = False
    return not increasing and not decreasing

def euler112():
    n = 1
    countBouncy = 0
    countTotal = 0
    while True:
        if isBouncy(n):
            countBouncy += 1
        countTotal += 1
        percent = countBouncy / countTotal * 100.0
        if percent >= 99.0:
            print("Result = ", n, percent)
            break
        n += 1
        
if __name__ == "__main__":
    timedRun(euler112)
