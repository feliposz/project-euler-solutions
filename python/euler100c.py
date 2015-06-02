from fractions import Fraction
from math import sqrt
from time import time


start = time()
last_display = start

sqrt2 = 2**0.5 #sqrt(2)
blue = int(10**12 / sqrt2)

while True:
    total = int(blue * sqrt2)
    red = total - blue

    num = blue * (blue - 1)
    den = total * (total - 1)

    #print(total, blue, red, num/den)

    if time() - last_display > 60:
        print("[Progress] Blues: %d Reds: %d Total: %d Time: %d" %
              (blue, red, total, int(time() - start)))
        last_display = time()

    if num * 2 == den:
        print("Blues: %d Reds: %d Total: %d Time: %f" %
              (blue, red, total, time() - start))
        if total >= 10**12:
            break
    blue += 1

