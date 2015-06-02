"""Problem 113
10 February 2006

Working from left-to-right if no digit is exceeded by the digit to its
left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases
such that there are only 12951 numbers below one-million that are not
bouncy and only 277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?
"""

from eulerlib import timedRun
import math

#http://pt.wikipedia.org/wiki/Arranjo_(matem%C3%A1tica)#Combina.C3.A7.C3.A3o_simples
def combinations(n, k):
    assert n >= 0 and k >= 0, "Both n and k should be >= 0 for combinations."
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

#http://pt.wikipedia.org/wiki/Arranjo_(matem%C3%A1tica)#Combina.C3.A7.C3.A3o_com_repeti.C3.A7.C3.A3o
def combinationsWithRepetition(n, k):
    assert n >= 0 and k >= 0, "Both n and k should be >= 0 for combinations."
    return math.factorial(n+k-1) / (math.factorial(k) * math.factorial(n - 1))

def euler113():
    increasingCount = 0
    decreasingCount = 0
    for digits in range(1, 101):
        increasingCount += combinationsWithRepetition(9, digits)
        decreasingCount += (combinationsWithRepetition(10, digits) - 10)
    print(increasingCount + decreasingCount)

if __name__ == "__main__":
    timedRun(euler113)
