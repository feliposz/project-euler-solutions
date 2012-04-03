##Problem 39
##14 March 2003
##
##If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
##
##{20,48,52}, {24,45,51}, {30,40,50}
##
##For which value of p  1000, is the number of solutions maximised?

import math

solutions = {}

for a in range(1, 1000):
    for b in range(1, 1000):
        h = math.sqrt(a*a + b*b)
        if h == math.trunc(h):
            p = int(a+b+h)
            if p <= 1000:
                solutions[p] = solutions.get(p, 0) + 1

most_solutions = 0
top_k = 0
for k in solutions.keys():
    if solutions[k] > most_solutions:
        most_solutions = solutions[k]
        top_k = k

print(top_k)
