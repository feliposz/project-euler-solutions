"""Arithmetic expressions
Problem 93
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making
use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it
is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can
be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set
of consecutive positive integers, 1 to n, can be obtained, giving your answer
as a string: abcd.
"""

from eulerlib import generateListPermutations, timedRun

generated = {}

def getPermutations(a, b, c, d):
    return generateListPermutations([a,b,c,d])

def allGroupings(m):
    a, b, c, d = m
    # only need to deal with parenthesized cases...
    # realized that after reading grimbal post at http://projecteuler.net/thread=93
    g0 = "(({0} op1 {1}) op2 {2}) op3 {3}".format(a,b,c,d)
    g1 = "({0} op1 {1}) op2 ({2} op3 {3})".format(a,b,c,d)
    g2 = "({0} op1 ({1} op2 {2})) op3 {3}".format(a,b,c,d)
    g3 = "{0} op1 (({1} op2 {2}) op3 {3})".format(a,b,c,d)
    g4 = "{0} op1 ({1} op2 ({2} op3 {3}))".format(a,b,c,d)
    return [g0, g1, g2, g3, g4]

def allOperations():
    op = "+-*/"
    combos = []
    for i in range(64):
        a = i // 16
        b = i // 4 % 4
        c = i % 4
        combos.append((op[a], op[b], op[c]))
    return combos

def applyPatterns(a, b, c, d):
    ops = allOperations()
    for p in getPermutations(a, b, c, d):
        for g in allGroupings(p):
            for o in ops:
                expr = g.replace("op1", o[0]).replace("op2", o[1]).replace("op3", o[2])
                try:
                    v = eval(expr)
                    iv = int(v)
                    # count only positive integer results
                    if v == iv and iv > 0:
                        generated[iv] = True
                except ZeroDivisionError:
                    # don't count zero division
                    None

def countConsecutive():
    global generated
    consecutive = 1
    maxConsecutive = 0
    k = list(generated.keys())
    prev = k[0]
    for i in k:
        if i == prev+1:
            consecutive += 1
            if consecutive > maxConsecutive:
                maxConsecutive = consecutive
        else:
            consecutive = 1
        prev = i
    return maxConsecutive

def euler93():
    global generated
    maxConsecutive = 0
    sequence = ()
    for a in range(1,10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):
                    generated = {}
                    applyPatterns(a, b, c, d)
                    consecutive = countConsecutive()
                    print(a, b, c, d, consecutive)
                    if consecutive > maxConsecutive:
                        maxConsecutive = consecutive
                        sequence = (a, b, c, d)
    return sequence

print("result:", timedRun(euler93))

# TODO: reimplement this using Reverse Polish Notation to evaluate the
# expressions and string permutations of 4 digits and 3 operators, thus
# eliminating the need for parenthesis


