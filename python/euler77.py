"""Problem 77
27 August 2004

It is possible to write ten as the sum of primes in exactly five
different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in
over five thousand different ways?
"""

##(define (count-change value)
##  (define (combine value coins)
##    (cond ((empty? coins) 0)
##          ((= value 0) 1)
##          ((< value (first coins)) (combine value (rest coins)))
##          (else (+ (combine (- value (first coins)) coins)
##                   (combine value (rest coins))))))
##  (combine value (list 200 100 50 20 10 5 2 1)))

from eulerlib import generatePrimesSieve

LIMIT = 1000000
primes, isPrime = generatePrimesSieve(LIMIT)

def countAddendCombinations(num, addends):
    """Count how many combinations of addends can add to the value of 'num'.

    Parameters:
    'num' must be positive.
    'addends' must be sorted.
    """
    if len(addends) == 0:
        return 0
    elif num == 0:
        return 1
    elif num < addends[-1]:
        return countAddendCombinations(num, addends[:-1])
    else:
        lastRemoved = countAddendCombinations(num, addends[:-1])
        lastSubtracted = countAddendCombinations(num - addends[-1], addends)
        return lastRemoved + lastSubtracted

def countPrimeCombinatinos(num):
    """Count how many combination of primes can be added to the value of 'num'.

    Parameters:
    'num' must be positive.
    """
    assert num >= 0, "'num' must be positive."
    addends = [n for n in primes if n < num]
    return countAddendCombinations(num, addends)

def euler77():
    """Solves problem 77 from Project Euler."""
    n = 1
    while True:
        c = countPrimeCombinatinos(n)
        print("Num:", n, " Count:", c)
        if c >= 5000:
            break
        n += 1
    
if __name__ == "__main__":
    euler77()
