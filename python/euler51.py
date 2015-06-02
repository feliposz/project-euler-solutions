"""Problem 51
29 August 2003
http://projecteuler.net/problem=51

By replacing the 1st digit of *3, it turns out that six of the nine
possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443,
56663, 56773, and 56993. Consequently 56003, being the first member of
this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""

from eulerlib import generatePrimesSieve, timedRun

# Limit to the prime number generator (1 million is enough for this
# particular case).
LIMIT = 1000000

# Expected size of family of prime numbers with replaceable digits
FAMILY_SIZE = 8

primes, isPrime = generatePrimesSieve(LIMIT)

def euler51():
    """Solve problem 51 from Project Euler."""

    # Check all prime numbers
    for p in primes:
        # Check if number can generate other primes by replacing a
        # single digit
        count = countSingleDigitReplacements(p)
        if count == FAMILY_SIZE:
            print(p)
            break

        # Check if number can generate other primes by replacing
        # multiple repeated (possibly non-adjacent) digits
        count = countRepeatedDigitReplacements(p)
        if count == FAMILY_SIZE:
            print(p)
            break

def countSingleDigitReplacements(p):
    """Count how many primes can be generated at most by replacing a
    single digit of the given number."""
    
    s = str(p)
    max_count = 0

    # Don't replace the last digit. This makes sense, since replacing
    # it would make the number non-prime in most of the cases anyway.
    
    for i in range(len(s) - 1):
        count = 0
        for digit in range(10):
            # Replace a single digit at position
            new_s = s[:i] + str(digit) + s[i+1:]
            # Don't count number if first digit was replaced by 0
            if new_s[0] != '0' and isPrime[int(new_s)]:
                count += 1
        max_count = max(max_count, count)
        
    return max_count

def countRepeatedDigitReplacements(p):
    """Count how many primes can be generated at most by replacing
    multiple repeated (possibly non-adjacent) digits on the given
    number."""
    
    s = str(p)
    
    # check for replaceable repeated digits
    digit_count = {}
    for c in s:
        digit_count[c] = digit_count.get(c, 0) + 1

    max_count = 0
    for c in digit_count:
        if digit_count[c] > 1: # found repeated digits
            count = 0
            for digit in range(10):
                # Replace all repeated occurrences
                new_s = s.replace(c, str(digit))
                # Don't count number if first digit was replaced by 0
                if new_s[0] != '0' and isPrime[int(new_s)]:
                    count += 1
            max_count = max(max_count, count)

    return max_count

if __name__ == "__main__":              
    timedRun(euler51)
