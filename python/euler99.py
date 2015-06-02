##from eulerlib import generatePrimesSieve
##
##primes = []
##
### Not sure if this is a great way to factorate
##def factorate(num):
##    """Return factors for a given number"""
##    if num < 2:
##        return {}
##    factors = {}
##    for p in primes:
##        #if (primes[-1] < num): # generate only as many primes as necessary
##        #    primes.append(next(primes_gen))
##        while (num % p) == 0:
##            num /= p
##            factors[p] = factors.get(p, 0) + 1
##        if num == 1:
##            break
##    return factors


# TODO: This is extremely slow! It took 2610 seconds (43 minutes!) to
# find the solution. There must be a much better, more efficient way
# to compare very large exponentiations. Find out and REDO this thing!

import time

start = time.time()
line_num = 0
highest_line = 0
highest_num = 0
highest_pair = (0,0)
file = open("base_exp.txt")
while True:
    line = file.readline()
    if not line: break
    line_num += 1
    base, exp = tuple(map(int, line.split(",")))
    num = base**exp
    if num > highest_num:
        highest_num = num
        highest_line = line_num
        highest_pair = (base, exp)
    print("line =", line_num, "time =", time.time() - start, "pair =", highest_pair)
file.close()
print(highest_line, highest_pair)

##primes, isPrime = generatePrimesSieve(highest_exp + 1)
