"""Problem 124
14 July 2006

The radical of n, rad(n), is the product of distinct prime factors of
n. For example, 504 = 2³ * 3² * 7, so rad(504) = 2 * 3 * 7 = 42.

If we calculate rad(n) for 1 <= n <= 10, then sort them on rad(n), and
sorting on n if the radical values are equal, we get:

Unsorted     Sorted

n rad(n)    n rad(n) k
1   1       1   1    1
2   2       2   2    2
3   3       4   2    3
4   2       8   2    4
5   5       3   3    5
6   6       9   3    6
7   7       5   5    7
8   2       6   6    8
9   3       7   7    9
10  10      10  10   10

Let E(k) be the kth element in the sorted n column; for example, E(4)
= 8 and E(6) = 9.

If rad(n) is sorted for 1 <= n <= 100000, find E(10000).
"""

from eulerlib import generatePrimesSieve, timedRun

LIMIT = 100000
print("Build primes")
primes, isPrime = generatePrimesSieve(LIMIT)

def rad(n):
    if n == 0:
        return 0
    r = 1
    for p in primes:
        if n == 0 or p > n:
            break
        if n % p == 0:
            r *= p
            while n > 0 and n % p == 0:
                n //= p
    return r

def euler124():
    print("Build radList")
    radList = [] #0th element is (0, 0)
    for n in range(LIMIT+1):
        element = (rad(n), n)
        radList.append(element)
        if n % 10000 == 0:
            print(n // 1000, "%")

    print("Sort radList")
    radList = sorted(radList)

    print("Last element (rad(n), n):", radList[10000])

if __name__ == "__main__":
    timedRun(euler124)
