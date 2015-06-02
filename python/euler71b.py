from fractions import gcd, Fraction
import time

proper = []

LIMIT = 1000000

n = LIMIT // 7 * 3
d = LIMIT // 3 * 3

f37 = Fraction(3, 7)

start = time.time()

print("Generating proper fractions below 3/7")
while n > 0 and d > 0:
    d -= 1
    while Fraction(n, d) >= f37:
        n -= 1
    if d < LIMIT and gcd(n, d) == 1:
        proper.append(Fraction(n, d))
print("Generating time =", time.time() - start)

print("Sorting")
sorted_proper = sorted(proper)
print("Total time = ", time.time() - start)

print(sorted_proper[-1])
