"""Problem 43
09 May 2003

Find the sum of all pandigital numbers with an unusual sub-string
divisibility property.

The number, 1406357289, is a 0 to 9 pandigital number because it is
made up of each of the digits 0 to 9 in some order, but it also has
a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this
way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from eulerlib import generateStringPermutations, timedRun

# NOT_TO_DO: maybe create a permutations generator, and test 1 by 1
# to avoid using so much memory???
# INSTEAD: check euler43b =D

def euler43():
    """Very slow solution for problem 43 of Project Euler."""
    print("Generating permutations...", end="")
    pandigitals = generateStringPermutations("0123456789")
    print("done")
    divisors = [1, 2, 3, 5, 7, 11, 13, 17]

    total = 0
    for p in pandigitals:
        ok = True
        for i in range(0, 8):
            num = int(p[i:i+3])
            if num % divisors[i] != 0:
                ok = False            
                break
        if ok:
            total += int(p)
            print(p)
    print("Total =", total)

#Another possibility is:
#  to generate only the multiples of 17 with 3 digits
#  then generate only the multiples of 13 with 3 digits and with the
#    the last 2 digits = first 2 digits of the 17 multiples
#  ...
#  generate all multiples of 2 that have
#    the last 2 digits = first 2 digits of the remaining 3 multiples


def genMultiplesStr(factor):
    """Generate a list with all multiples of factor up to 1000 normalized
    to 3 digit strings."""
    multiples = []
    for n in range(factor, 1000, factor):
        s = ("00" + str(n))[-3:]
        multiples.append(s)
        n += factor
    return multiples

def mergeMultiples(oldlist, newlist):
    """Creates a new list only with members of oldist whose first 2 digits
    match with the last 2 digits of the newlist."""
    candidates = {}
    for old in oldlist:
        for new in newlist:
            if old[:2] == new[-2:]:
                s = new[0] + old
                candidates[s] = 1
    return list(candidates.keys())

def isPandigital10(s):
    """Check if number is pandigital from 0-9, i.e. that it has all digits
    from 0 to 9."""
    if len(s) != 10:
        return False
    for i in range(0, 10):
        if s.find(str(i)) == -1:
            return False
    return True

def euler43b():
    """A better solution for problem 43 of Project Euler"""
    # Generates numbers only with valid multiples    
    candidates = genMultiplesStr(17)
    # TODO: The time consuming part is for factor = 1
    # Should find a way to take the list generated after factor = 2,
    # remove all the numbers with repeating factors,
    # add the remaining digit to the number in the remaining list
    # voilà!
    # Guess this would take less than a second
    for factor in [13, 11, 7, 5, 3, 2, 1]:        
        newlist = genMultiplesStr(factor)
        candidates = mergeMultiples(candidates, newlist)
    # Sum only the pandigitals 0-9
    total = 0
    for c in candidates:
        if isPandigital10(c):
            total += int(c)
    print("Total =", total)
            
if __name__ == "__main__":
    timedRun(euler43b)

