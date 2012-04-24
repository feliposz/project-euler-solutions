"""Problem 95
13 May 2005

The proper divisors of a number are all the divisors excluding the
number itself. For example, the proper divisors of 28 are 1, 2, 4, 7,
and 14. As the sum of these divisors is equal to 28, we call it a
perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum
of the proper divisors of 284 is 220, forming a chain of two numbers.
For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with
12496, we form a chain of five numbers:

12496 ->  14288 -> 15472 -> 14536 -> 14264 ( 12496  ...)

Since this chain returns to its starting point, it is called an
amicable chain.

Find the smallest member of the longest amicable chain with no element
exceeding one million.
"""

from eulerlib import timedRun

# Global initializations

LIMIT = 1000000

print("Generating list of sum of proper divisors")
divisors = [0] * LIMIT
for div in range(1, LIMIT):
    for step in range(div, LIMIT, div):
        if step != div:
            divisors[step] += div

# Functions

def countChain(num):
    """Returns chain length and lowest element."""
    chain = [num]
    nextChain = num
    while True:
        nextChain = divisors[nextChain]
        if nextChain == num:
            return len(chain), min(chain)
        if nextChain == 0 or nextChain >= LIMIT or nextChain in chain:
            return 0, 0 # not amicable
        chain.append(nextChain)

def euler95():
    print("Searching for the longest chain")
    max_count = 0
    lowest_elem = 0
    for n in range(1, 1000000):
        count, lowest = countChain(n)
        if count > max_count:
            print("Longest found: ", n, count, lowest)
            max_count = count
            lowest_element = lowest

if __name__ == "__main__":
    timedRun(euler95)
