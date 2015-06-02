from fractions import Fraction
from math import sqrt
from time import time

# Looking at the data, I stumbled upon 2 "magic" numbers for this
# problem.

# One is the ratio blue chips / total chips that converges to sqrt(2).
# So I use an approximation to get the value of total based on the
# current estimate for blue chips.

# The other is the ratio between two successive exact solutions.
# For example:
# Blue    Reds    Totals
# 2871    1189    4060
# 16731   6930    23661

# The tree ratios quickly converge to 5,8284...
# 5,827586207	5,82842725	5,827832512

# I took advantage of this to find the next solution very quickly


start = time()
last_display = start

sqrt2 = 2 ** 0.5

sqrt2num = int(sqrt2 * 10**16)
sqrt2den = 10**16

blue = 15

while True:
    total = blue * sqrt2num // sqrt2den
    red = total - blue

    num = blue * (blue - 1)
    den = total * (total - 1)

    #print(total, blue, red, num/den)

    if num * 2 == den:
        print("Blues: %d Reds: %d Total: %d Time: %f" %
              (blue, red, total, time() - start))

        # MAGIC number... actually, if I improve the precision, it
        # "skips" some numbers. I don't know why yet...        
        blue = blue * 582842 // 100000 - 1

        if total >= 10**12:
            break

    # Last "MAGIC" improvement didn't land on a solution, increase 1
    # and try it    
    blue += 1


