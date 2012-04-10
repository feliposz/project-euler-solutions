from fractions import gcd, Fraction
import time

proper = []

start = time.time()

# Too slow for values larger than 1000, check euler71b.py

print("Generating proper fractions")
LIMIT = 1000
for d in range(1, LIMIT + 1):
    for n in range(1, d):
        if gcd(n, d) == 1:
            proper.append(Fraction(n, d))
print("Time = ", time.time() - start)

print("Sorting")
sorted_proper = sorted(proper)
print("Time = ", time.time() - start)

index = sorted_proper.index(Fraction(3, 7))
print("Fraction to the left of 3/7: ", sorted_proper[index - 1])

