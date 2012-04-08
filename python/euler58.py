"""Problem 58
05 December 2003

Starting with 1 and spiralling anticlockwise in the following way, a
square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom
right diagonal, but what is more interesting is that 8 out of the 13
numbers lying along both diagonals are prime; that is, a ratio of 8/13
62%.

If one complete new layer is wrapped around the spiral above, a square
spiral with side length 9 will be formed. If this process is
continued, what is the side length of the square spiral for which the
ratio of primes along both diagonals first falls below 10%?
"""
from eulerlib import countPrimes, timedRun

def squareSpiralCorners(side):
    """Returns the four corners of a spiral square in the given side length.

    The corners are returned in a tuple in the order:
    (topRight, topLeft, bottomLeft, bottomRight)
    """
    botR = side * side
    botL = botR - side + 1
    topL = botL - side + 1
    topR = topL - side + 1
    return (topR, topL, botL, botR)

def euler58():
    """Solve problem 58 from Project Euler."""
    side = 1
    numbers = 1
    nprimes = 0
    while True:
        side += 2
        tr, tl, bl, br = squareSpiralCorners(side)
        #bottom right is never prime (sideLength²)
        nprimes += countPrimes([tr, tl, bl])
        numbers += 4
        ratio = nprimes / numbers
        if ratio < 0.1:
            print(nprimes, numbers, ratio)
            print("side length = ", side)
            break
        
if __name__ == "__main__":
    timedRun(euler58)
