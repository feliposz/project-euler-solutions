from fractions import Fraction

# I thought about using continued fractions to calculate a value for
# the blues and totals, since the ratio total / ratio successively
# approximates to sqrt(2), but the interval appears to be too far from
# the answer.

den = 1
while True:
    den = 2 + Fraction(1, den)
    if den.numerator > 1000000000000:
        break
    rad = 1 + Fraction(1, den)
    print(rad * 1.0, rad)


##707106781186
##...
##886731088897
##
##
##(707106781186 / 1000000000000) * (707106781185 / 999999999999)
##0,49999999999901857678540901857679
##
##(886731088897 / 1254027132096) * (886731088896 / 1254027132095)
##0,49999999999983484665053478242822
