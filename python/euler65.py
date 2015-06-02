"""Problem 65
12 March 2004
http://projecteuler.net/problem=65

The square root of 2 can be written as an infinite continued fraction.

sqrt(2) = 1 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))

The infinite continued fraction can be written, sqrt(2) = [1;(2)], (2)
indicates that 2 repeats ad infinitum. In a similar way, sqrt(23) =
[4;(1,3,1,8)].

It turns out that the sequence of partial values of continued
fractions for square roots provide the best rational approximations.
Let us consider the convergents for 2.

1 + 1/2 = 3/2
1 + 1/(2 + 1/2) = 7/5
1 + 1/(2 + 1/(2 + 1/2) = 17/12
1 + 1/(2 + 1/(2 + 1/(2 + 1/2) = 41/29

Hence the sequence of the first ten convergents for 2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985,
3363/2378, ... What is most surprising is that the important
mathematical constant, e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1,
...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is
1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.

"""

from fractions import Fraction
from eulerlib import sumDigits

#LIMIT = 0 -> 1st convergent
#LIMIT = 9 -> 10th convergent
#LIMIT = 99 -> 100th convergent
LIMIT = 99

# For a clearer representation, check:
# http://en.wikipedia.org/wiki/E_(mathematical_constant)#Representations


# Generate sequence = [1, 2, 1,   1, 4, 1,   1, 6, 1, ...]
seq = []
n = 1
while len(seq) < LIMIT:
    seq += [1, 2*n, 1]
    n += 1

# To generate the (N+1)th convergent, start from the (N-1)th and go
# backwards to the 0th in the sequence.

# Calculate from the lowest denominator... _________
#                                                |||
#                                                vvv
# (1 + 1/(2 + 1/(1 + 1/(1 + 1/(4 + 1/(1 + 1/(1 + ...)))))))

den = Fraction(0, 1)
for i in range(LIMIT-1, -1, -1):
    if den == Fraction(0, 1):
        den = Fraction(seq[i], 1)
    else:
        den = Fraction(seq[i], 1) + Fraction(1, den)

if LIMIT == 0:
    e = Fraction(2, 1)
else:
    e = Fraction(2, 1) + Fraction(1, den)

print(e)
print(sumDigits(e.numerator))
