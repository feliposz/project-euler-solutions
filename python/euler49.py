"""Problem 49
01 August 2003

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of
one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in
this sequence?
"""

from eulerlib import generatePrimesLimit, generateStringPermutations, isPrime

primes = generatePrimesLimit(10000)

for prime in primes:
    #should check above 1000 only?
    permutations = generateStringPermutations(("000"+str(prime))[-4:])
    # create a list only with permutations that are also prime
    prime_permutations = []
    for permutation in permutations:
        if len(permutation) == 4 and isPrime(int(permutation)):
            prime_permutations.append(int(permutation))
    if len(prime_permutations) > 2:
        sorted_pp = sorted(prime_permutations)
        # this trick avoid checking permutations twice
        if int(sorted_pp[0]) < prime:
            continue
        # compare all members to see if there are 3 in an arithmetic progression
        difs = []        
        for pp1 in sorted_pp:
            goOut = False
            for pp2 in sorted_pp:
                if pp1 < pp2:
                    dif = pp2 - pp1
                    if dif in difs and pp1 - dif in sorted_pp:
                        # Found another pair with the same difference...
                        print(pp1 - dif, pp1, pp2, "dif =", dif)
                        goOut = True
                        break
                    difs.append(dif)
            if goOut:
                break

