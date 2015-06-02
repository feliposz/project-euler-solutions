from fractions import Fraction, gcd
from math import sqrt
from time import time


start = time()
last_display = start

sqrt2 = 2**0.5 #sqrt(2)
blue = 15 #int(10**1 / sqrt2)

while True:
    total = int(blue * sqrt2)
    red = total - blue

    if time() - last_display > 60:
        print("[Progress] Blues: %d Reds: %d Total: %d Time: %d" %
              (blue, red, total, int(time() - start)))
        last_display = time()

    div1 = gcd(blue, total)
    div2 = gcd(blue - 1, total - 1)
    if div1 > 1 and div2 > 1:
        blue1 = blue // div1
        total1 = total // div1
        blue2 = (blue - 1) // div2
        total2 = (total - 1) // div2

        num = blue1 * blue2
        den = total1 * total2

        if num * 2 == den:
            print("Blues: %d Reds: %d Total: %d Time: %f" %
                  (blue, red, total, time() - start))
            print(div1, div2)
            if total >= 10**12:
                break

    blue += 1

