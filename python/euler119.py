from eulerlib import sumDigits
from time import time
import math

start = time()

a = [None]

##count = 0
##num = 10
##while len(a) <= 30:
##    base = sumDigits(num)
##    power = base
##    if power > 1:
##        while power <= num:
##            power *= base
##            if power == num:
##                count += 1
##                print("Count: %d Num: %d Base: %d Time: %d" %
##                      (count, num, base, time() - start))
##                a.append(num)
##                break
##    num += 1
    
##1 81 9
##2 512 8
##3 2401 7
##4 4913 17
##5 5832 18
##6 17576 26
##7 19683 27
##8 234256 22
##9 390625 25
##10 614656 28
##11 1679616 36
##12 17210368 28

candidates = []

for base in range(2, 100):
    for expt in range(1, 100):
        num = base ** expt
        if num >= 10 and base == sumDigits(num):
            candidates.append(num)

print("Elements generated:", len(candidates))

candidates.sort()

print("a 2 =", candidates[1])
print("a 10 =", candidates[9])
print("a 30 =", candidates[29])


print("Time:", time() - start)
        
