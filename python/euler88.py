"""Product-sum numbers
Problem 88
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 * a2 * ... * ak.

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 * 2 = 2 + 2
k=3: 6 = 1 * 2 * 3 = 1 + 2 + 3
k=4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2<=k<=6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2<=k<=12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2<=k<=12000?
"""

import operator
from itertools import combinations_with_replacement
from functools import reduce
from fractions import gcd
#from prime_decomposition import decompose

minimal = {}

#UPPER = 12000

#minimal = [k*2 for k in range(0, UPPER)]
#minimal[1] = 0
                                           



def divisors(n):
    return [ d for d in range(1, n//2+1) if n % d == 0 ]

def prod(iterable):
    return reduce(operator.mul, iterable, 1)
    
def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors
    
#for n in range(2, 30):
#    factors = prime_factors(n)
#    if len(factors) > 1 and sum(factors) <= n:
#        print('%d => %s' % (n, str(factors)))
for k in range(2, 12):
    for comb in combinations_with_replacement(divisors(k*2), k):
        p = prod(comb)
        s = sum(comb)
        if p == s and (k not in minimal or minimal[k] > s):
            minimal[k] = s
            print('k = %d, result = %d, set => %s' % (k, s, str(comb)))


#for n in range(2, 30):
#    #print(n)
#    for k in range(2, 30):
#        for comb in combinations_with_replacement(divisors(n), k):
#            p = prod(comb)
#            s = sum(comb)
#            #print('c=%s, s=%d, p=%d ' % (str(comb), s, p))
#            #if s > n or p > n:
#            #    break
#            if s == n and p == n:            
#                if k not in minimal or minimal[k] > s:
#                    minimal[k] = s
#                    print('k = %d, result = %d, set => %s' % (k, s, str(comb)))

for k, v in minimal.items():
    print('k = %d, v = %d' % (k, v))

#for k, v in minimal.items():
#    print('k = %d, v = %d' % (k, v))

    
# NOTE: just some experiments
# TODO: try to improve on these ideas

