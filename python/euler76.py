"""Problem 76
13 August 2004

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at
least two positive integers?
"""

# Detailed explanation for this pair of functions:
# http://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function

##One way of getting a handle on the partition function involves an
##intermediate function p(k, n), which represents the number of
##partitions of n using only natural numbers at least as large as k.
##For any given value of k, partitions counted by p(k, n) fit into
##exactly one of the following categories:
##
## 1) smallest addend is k;
## 2) smallest addend is strictly greater than k.
##
##The number of partitions meeting the first condition is p(k, n − k).

# Memoization makes this recursive function MUCH faster
memo = {}
def pkn(k, n):
    if k > n: return 0
    if k == n: return 1
    if not memo.get((k, n)):
        memo[(k, n)] = pkn(k + 1, n) + pkn(k, n - k)
    return memo[(k, n)]

#In number theory, the partition function p(n) represents the number
#of possible partitions of a natural number n, which is to say the
#number of distinct (and order independent) ways of representing n as
#a sum of natural numbers. By convention p(0) = 1, p(n) = 0 for n
#negative.

def p(n):
    return 1 + sum([pkn(k, n - k) for k in range(1, n//2 + 1)])

# -1 to discard 100 itself
print(p(100) - 1)
    
