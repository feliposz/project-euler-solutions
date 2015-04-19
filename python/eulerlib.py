"""This library is used by several scripts for solving problems in the
Project Euler site."""

import time
import math

def generateNPrimes(nprimes):
    """Returns a list of primes with 'nprimes' elements.

    Generate primes by creating a list and trying to divide every odd number
    by members of the list generated so far. This is not very efficient!
    """
    # TODO: Improve this algorithm
    assert type(nprimes) == type(1), "'nprimes' must be an integer."
    primes = [2,]
    num = 3
    count = 1
    while (count < nprimes):
        prime = True
        for div in primes:
            if num % div == 0:
                prime = False
                break
        if prime:
            primes.append(num)
            count += 1
        num += 2
    return primes

def generateNPrimes2(nprimes):
    """Returns a list of primes with 'nprimes' elements.
    Performance isn't great.
    """
    assert type(nprimes) == type(1), "'nprimes' must be an integer."
    primes = [2,]
    count = 1
    num = 3
    while count < nprimes:
        if isPrime(num):
            primes.append(num)
            count += 1
        num += 2
    return primes

def generatePrimesLimit(limit):
    """Generate a list of primes up to 'limit'.

    The list is generated testing each element for primeness.
    Performance isn't great. Use generatePrimesSieve instead.
    """
    assert type(limit) == type(1), "'limit' must be an integer."
    primes = [2,]
    for num in range(3, limit+1, 2):
        if isPrime(num):
            primes.append(num)
    return primes

def generatePrimesSieve(limit):
    """Returns a tuple with a list of primes up to 'limit' and a list
    of booleans of size 'limit' for primality test.

    Examples:
    primes, isPrime = generatePrimesSieve(10)

    Values returned are:
    primes = [2, 3, 5, 7]
    isPrime = [False, False, True, True, False, True, False, True,
               False, False]

    The lists are generated using the Sieve of Eratosthenes.
    """
    #http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    assert limit <= 100000010, "I'm not sure there will be enough memory for a table of this size. Sorry. =("
    primeTable = [None for i in range(limit)]
    primeTable[2] = True
    for p in range(3, limit, 2): # only check odds
        if primeTable[p] is None:
            primeTable[p] = True
            sieve = p * p # no need to mark below p^2
            while sieve < limit:
                primeTable[sieve] = False
                sieve += p * 2 # 2* because of skipping even numbers...
    primes = []
    for num in range(limit):
        if primeTable[num]:
            primes.append(num)
        else:
            primeTable[num] = False
    return (primes, primeTable)

# Algorithm described in Project Euler - Problem 7
# http://projecteuler.net/project/resources/007_c1bfcd3425fd13f6e9abcfad4a222e35/007_overview.pdf
def isPrime(n):
    """Return if n is a prime number.

    This is reasonably fast for individual tests. If testing many numbers,
    consider generating a table. See generatePrimesSieve.
    """
    assert type(n) == type(1), "'n' must be an integer."
    if n <= 1: # negatives, 0 and 1 are not primes
        return False
    elif n < 4:
        return True  # 2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True  # we have already excluded 4, 6 and 8.
    elif n % 3 == 0:
        return False
    else:
        # n rounded to the greatest integer r so that r*r<=n
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f = f + 6
        return True # in all other cases

def countPrimes(numList):
    """Count how many numbers in the list are primes.

    The numbers are tested with the isPrime function and is fast for testing
    sparse numbers. For sequential testing it's better to generate a table
    of primes.
    """
    count = 0
    for num in numList:
        if isPrime(num):
            count += 1
    return count

def timedRun(function):
    """Returns the same value returned by 'function'.

    Run 'function' and print the execution time at the end.
    """
    assert type(function) == type(timedRun), "'function' must be a function."
    startTime = time.time()
    startClock = time.clock()
    result = function()
    print()
    print("Run time for execution of", function.__name__)
    print("Using time.time() =", time.time() - startTime)
    print("Using time.clock() =", time.clock() - startClock)
    return result

def sumDigits(digits):
    """Return the sum of all the digits in 'digits'."""
    if type(digits) == type(""):
        s = digits
    else:
        s = str(digits)
    total = 0
    for c in s:
        total += int(c)
    return total

def generateListPermutations(elements, level=0):
    """Generate all possible permutations of the list 'elements'."""
    #print("  " * level, "gP(", elements, ")")
    if len(elements) == 0:
        return [[]]
    permutations = []
    for e in elements:
        reduced = elements[:]
        reduced.remove(e)
        reducedPermutations = generateListPermutations(reduced, level + 1)
        #print(" "*level, "reduced", reducedPermutations)
        for p in reducedPermutations:
            p.insert(0, e)
            permutations.append(p)
    return permutations

def generateStringPermutations(string, level=0):
    """Generate all possible permutations of the 'string'."""
    if len(string) == 0:
        return [""]
    permutations = []
    for c in string:
        reduced = string.replace(c, "", 1)
        reducedPermutations = generateStringPermutations(reduced, level + 1)
        for p in reducedPermutations:
            permutations.append(c + p)
    return permutations

# Extracted from: http://stackoverflow.com/a/2837693

def generateCombinationsIter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in generateCombinationsIter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next

def generateCombinations(l, k):
    return list(generateCombinationsIter(l, k))

def triangleNum(n):
    """Returns the nth triangle number."""
    return int(n * (n + 1) / 2)

def squareNum(n):
    """Returns the nth square number."""
    return int(n * n)

def pentagonalNum(n):
    """Returns the nth pentagonal number."""
    return int(n * (3*n - 1) / 2)

def hexagonalNum(n):
    """Returns the nth hexagonal number."""
    return int(n * (2*n - 1))

def heptagonalNum(n):
    """Returns the nth heptagonal number."""
    return int(n * (5*n - 3) / 2)

def octagonalNum(n):
    """Returns the nth octagonal number."""
    return int(n * (3*n - 2))

def isTriangleNum(n):
    """Tests if n is a triangle number."""
    d = 1 + 8 * n;
    if d < 0:
        return False
    x1 = (math.sqrt(d) - 1) / 2;
    return x1 >= 0.0 and x1 == math.floor(x1);

def isPentagonalNum(n):
    """Tests if n is a pentagonal number."""
    d = 1 + 24 * n;
    if d < 0:
        return False
    x1 = (1 + math.sqrt(d)) / 6;
    return x1 >= 0.0 and x1 == math.floor(x1);

def isHexagonalNum(n):
    """Tests if n is a hexagonal number."""
    d = 1 + 8*n;
    if d < 0:
        return False
    x1 = (1 + math.sqrt(d)) / 4;
    return x1 >= 0.0 and x1 == math.floor(x1);

def isPerfectSquare(n):
    x = int(math.sqrt(n)) #force to int to keep the precision
    return x * x == n

def isAlmostIsosceles(x, y):
    #a = b * h / 2
    #a = y/2 * math.sqrt(x*x - y*y/2) / 2 [??? something like that, can't remember]
    #a = math.sqrt(y*y * (x*x - y*y/4) / 4)  [but eventually it gets...]
    #a2 = y*y * (x*x - y*y/4) / 4
    #a2times4 = y*y * (x*x - y*y/4) [...to this]
    a2times16 = y*y * (4*x*x - y*y)
    if a2times16 % 16 != 0:
        return False
    a2 = a2times16 // 16
    return isPerfectSquare(a2)

# TODO: isHeptagonal, isOctogonal, isSquareNum (the simplest?)

def triangleArea(ax, ay, bx, by, cx, cy):
    """Returns the area of a triangle given its 3 vertices in
    cartesian coordinates.
    """
    # Formula found in:
    # http://www.mathopenref.com/coordtrianglearea.html

    return abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2

def pointInTriangle(point, trianglePoints):
    """Check if point is inside triangle described by trianglePoints.

    'point' is a tuple with format (x, y)
    'triaglePoints' is a tuple format (ax, ay, bx, by, cx, cy)
    """
    # This method was found in:
    # http://gmc.yoyogames.com/index.php?showtopic=172194

    ax, ay, bx, by, cx, cy = trianglePoints
    px, py = point
    original = triangleArea(ax, ay, bx, by, cx, cy)
    sub1 = triangleArea(ax, ay, bx, by, px, py)
    sub2 = triangleArea(ax, ay, px, py, cx, cy)
    sub3 = triangleArea(px, py, bx, by, cx, cy)
    return sub1 + sub2 + sub3 <= original

def reverseNum(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

def isNumPalindrome(num):
    return num == reverseNum(num)

def isReversible(n):
    """Returns true if a number is reversible.

    A number is reversible if the sum of n + reverseNum(n) produces a
    number with only odd digits.
    """
    if n % 10 == 0:
        return False
    s = n + reverseNum(n)
    while s > 0:
        digit = s % 10
        if not digit in [1,3,5,7,9]:
            return False
        s //= 10
    return True


#TODO: incorporate phi and factorate into eulerlib
#for my own implementation: euler243.py

# Possible candidates found at:
# http://freelancersunite.net/project_euler/project-euler-problem-243/
# Is it better not to use a list of primes in factorate?

##def factorate(n):
##        if n == 1: return [1]
##        i = 2
##        limit = n**0.5
##        while i <= limit:
##                if n % i == 0:
##                        ret = factor(n/i)
##                        ret.append(i)
##                        return ret
##                i += 1
##        return [n]
##
##def uniqify(seq):
##        return list(set(seq))
##
##def phi(x):
##    t = x
##    for k in uniqify(factorate(x)):
##        t -= t // k
##    return t

#TODO: Find a good way to incorporate Unit testing
#assert pointInTriangle((0, 0), (-340,495,-153,-910,835,-947)) == True, "Should be true."
#assert pointInTriangle((0, 0), (-175,41,-421,-714,574,-645)) == False, "Should be false."
