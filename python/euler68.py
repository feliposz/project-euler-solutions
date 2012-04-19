"""Problem 68
23 April 2004

Consider the following "magic" 3-gon ring, filled with the numbers 1
to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the
numerically lowest external node (4,3,2 in this example), each
solution can be described uniquely. For example, the above solution
can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10,
11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings;
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is
possible to form 16- and 17-digit strings. What is the maximum
16-digit string for a "magic" 5-gon ring?

"""

from eulerlib import generateListPermutations
import time

####Small concept test with 3-gon rings first
##
##def isValid3gon(nodes):
##    s0 = nodes[0] + nodes[1] + nodes[5]
##    s1 = nodes[1] + nodes[2] + nodes[3]
##    s2 = nodes[2] + nodes[0] + nodes[4]
##    return s0 == s1 and s0 == s2
##
##def sum3gon(nodes):
##    return nodes[0] + nodes[1] + nodes[5]
##
##def print3gon(nodes):
##    print("Total = ", sum3gon(nodes), end="\t")
##    print(nodes[3], ",", nodes[1], ",", nodes[2], end="; ")
##    print(nodes[4], ",", nodes[2], ",", nodes[0], end="; ")
##    print(nodes[5], ",", nodes[0], ",", nodes[1])
##
##def concat3gon(nodes):
##    s = ""
##    if nodes[3] < nodes[4] and nodes[3] < nodes[5]:
##        for i in [3, 1, 2, 4, 2, 0, 5, 0, 1]:
##            s += str(nodes[i])
##        return int(s)
##    else:
##        return None
##
##original3gon = [1, 2, 3, 4, 5, 6]
##perms = generateListPermutations(original3gon)
##high = 0
##for p in perms:
##    if isValid3gon(p):
##        #print3gon(p)
##        c = concat3gon(p)
##        if not c is None:
##            print(sum3gon(p), "\t", c)
##            if c > high:
##                high = c
##print(high)


def isValid5gon(nodes):
    s0 = nodes[0] + nodes[1] + nodes[7]
    s1 = nodes[1] + nodes[2] + nodes[8]
    s2 = nodes[2] + nodes[3] + nodes[9]
    s3 = nodes[3] + nodes[4] + nodes[5]
    s4 = nodes[4] + nodes[0] + nodes[6]
    return s0 == s1 and s0 == s2 and s0 == s3 and s0 == s4

def concat5gon(nodes):
    s = ""
    if nodes[9] < nodes[5] and nodes[9] < nodes[6] and nodes[9] < nodes[7] and nodes[9] < nodes[8]:
        for i in [9, 3, 2, 8, 2, 1, 7, 1, 0, 6, 0, 4, 5, 4, 3]:
            s += str(nodes[i])
        return int(s)
    else:
        return None

def sum5gon(nodes):
    return nodes[0] + nodes[1] + nodes[7]

def euler68():
    "Solves problem 68 from Project Euler."""

    start = time.time()

    print("Generating permutations... ", end="")
    original5gon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    perms = generateListPermutations(original5gon)
    print("done.")

    print("Time =", time.time() - start)

    print("Checking 5-gons:")
    high = 0
    for p in perms:
        if isValid5gon(p):
            c = concat5gon(p)
            if not c is None and len(str(c)) == 16:
                print(sum5gon(p), "\t", c)
                if c > high:
                    high = c
    print("Highest =", high)

    print("Time =", time.time() - start)

if __name__ == "__main__":
    euler68()
