"""Problem 69
07 May 2004

Euler's Totient function, φ(n) [sometimes called the phi function], is
used to determine the number of numbers less than n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n  10.

Find the value of n  1,000,000 for which n/φ(n) is a maximum.
"""

from eulerlib import timedRun
from fractions import gcd

def phi(num):
    count = 0
    for den in range(1, num):
        if gcd(num, den) == 1:
            count += 1
    return count

def euler69():
    """Solves problem 69 from Project Euler."""
    # At first I tried to bruteforce this. My algorithm was O(n²) and
    # was taking too long, so I decided to look at the data. I
    # perceived that everytime my program reached a maximum n/phi(n),
    # the value for 'n' was a product of consecutive primes. I decided
    # to just calculate the phi for the product of the consecutive
    # primes and found the answer quickly.
    primes = [2,3,5,7,11,13,17,19,23]
    maxim = 0
    n = 1
    for p in primes:
        n *= p
        if n > 1000000:
            break
        phi_n = phi(n)
        ratio = n / phi_n
        if ratio > maxim:
            maxim = ratio
            print(n, phi_n, ratio)      
    print("maxim =", maxim)

if __name__ == "__main__":
    timedRun(euler69)
