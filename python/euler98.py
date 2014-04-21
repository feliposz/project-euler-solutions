"""Anagramic squares
Problem 98
By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 362. What is remarkable is that,
by using the same digital substitutions, the anagram, RACE, also forms a square
number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and
specify further that leading zeroes are not permitted, neither may a different
letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, find all the square
anagram word pairs (a palindromic word is NOT considered to be an anagram of
itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""

from eulerlib import generateCombinations, isPerfectSquare
import itertools

dict = {}

def loadDict():

    # Read words from file. All are on a single line, delimited by " and split by ,
    file = open("words.txt")
    words = file.readline().strip().replace("\"","").split(",")
    file.close()

    # Create a hash table mapping all words that are anagrams
    for w in words:
        k = "".join(sorted(list(w)))
        if k in dict:
            dict[k].append(w)
        else:
            dict[k] = [w]

    # Remove words that have no anagrams
    for k in list(dict.keys()):
        if len(dict[k]) == 1:
            dict.pop(k)
        elif len(dict[k]) == 3:
            #special case, convert it into pairs
            a, b, c = dict[k]
            dict.pop(k)
            dict[a] = [a,b]
            dict[b] = [b,c]
            dict[c] = [a,c]

def checkPair(a, b):
    # get letters to substitute
    letters = "".join(sorted(list(a)))
    # generate all permutations for replacing
    permutations = itertools.permutations(list(range(10)), len(letters))

    for numbers in permutations:
        # replace each letter for a correspondingnumber
        s = a
        t = b
        for i in range(len(letters)):
            s = s.replace(letters[i], str(numbers[i]))
            t = t.replace(letters[i], str(numbers[i]))
        i = int(s)
        j = int(t)

        # check if numbers have same length (to eliminate leading zeroes)
        if len(str(i)) == len(str(j)):
            if isPerfectSquare(i) and isPerfectSquare(j):
                print(a, b, i, j)
                return max(i,j)
    return None

loadDict()
m = 0
for p in dict.values():
    a = p[0]
    b = p[1]
    r = checkPair(a,b)
    if r != None and r > m:
        m = r
print(m)

