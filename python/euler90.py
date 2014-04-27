"""Cube digit pairs
Problem 90
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:


In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""

import itertools

def isValidCombination(d1, d2):
    s01 = (0 in d1 and 1 in d2) or (0 in d2 and 1 in d1)
    s04 = (0 in d1 and 4 in d2) or (0 in d2 and 4 in d1)
    s09 = (0 in d1 and (6 in d2 or 9 in d2)) or (0 in d2 and (6 in d1 or 9 in d1))
    s16 = (1 in d1 and (6 in d2 or 9 in d2)) or (1 in d2 and (6 in d1 or 9 in d1))
    s25 = (2 in d1 and 5 in d2) or (2 in d2 and 5 in d1)
    s36 = (3 in d1 and (6 in d2 or 9 in d2)) or (3 in d2 and (6 in d1 or 9 in d1))
    s49 = (4 in d1 and (6 in d2 or 9 in d2)) or (4 in d2 and (6 in d1 or 9 in d1))
    s64 = ((6 in d1 or 9 in d1) and 4 in d2) or ((6 in d2 or 9 in d2) and 4 in d1) #curiosamente, igual a s49!
    s81 = (8 in d1 and 1 in d2) or (8 in d2 and 1 in d1)
    return s01 and s04 and s09 and s16 and s25 and s36 and s49 and s64 and s81

arrangements = list(itertools.combinations(range(10), 6))

count = 0
for d1 in arrangements:
    for d2 in arrangements:
        if d1 < d2 and isValidCombination(d1, d2):
                count += 1

print("len(arrangements)", len(arrangements))
print("count", count)

