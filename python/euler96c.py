"""Problem 96
27 May 2005

Su Doku (Japanese meaning number place) is the name given to a popular
puzzle concept. Its origin is unclear, but credit must be attributed
to Leonhard Euler who invented a similar, and much more difficult,
puzzle idea called Latin Squares. The objective of Su Doku puzzles,
however, is to replace the blanks (or zeros) in a 9 by 9 grid in such
that each row, column, and 3 by 3 box contains each of the digits 1 to
9. Below is an example of a typical starting puzzle grid and its
solution grid.

Puzzle:
0  0  3  0  2  0  6  0  0  
9  0  0  3  0  5  0  0  1  
0  0  1  8  0  6  4  0  0  
0  0  8  1  0  2  9  0  0  
7  0  0  0  0  0  0  0  8  
0  0  6  7  0  8  2  0  0  
0  0  2  6  0  9  5  0  0  
8  0  0  2  0  3  0  0  9  
0  0  5  0  1  0  3  0  0  

Solution:
4  8  3  9  2  1  6  5  7  
9  6  7  3  4  5  8  2  1  
2  5  1  8  7  6  4  9  3  
5  4  8  1  3  2  9  7  6  
7  2  9  5  6  4  1  3  8  
1  3  6  7  9  8  2  4  5  
3  7  2  6  8  9  5  1  4  
8  1  4  2  5  3  7  6  9  
6  9  5  4  1  7  3  8  2 

A well constructed Su Doku puzzle has a unique solution and can be
solved by logic, although it may be necessary to employ "guess and
test" methods in order to eliminate options (there is much contested
opinion over this). The complexity of the search determines the
difficulty of the puzzle; the example above is considered easy because
it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target
As...'), contains fifty different Su Doku puzzles ranging in
difficulty, but all with unique solutions (the first puzzle in the
file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found
in the top left corner of each solution grid; for example, 483 is the
3-digit number found in the top left corner of the solution grid
above.
"""

# TODO: BECOME LESS STUPID AND LEARN TO IMPLEMENT A PROPER SOLUTION
# FOR SUDOKU WITHOUT USING OTHER PEOPLE CODE!!!

file = open("sudoku.txt")

NGAMES = 50

def load_games():
    games = []
    for game in range(NGAMES):
        games.append([])
        s = file.readline()
        for row in range(9):
            s = file.readline()
            games[game].append([])
            for col in range(9):
                games[game][row].append(-int(s[col]))
    return games

# I suck... then I cheated
# From: http://www.alben.com/s.html / http://www.alben.com/sudoku1.py

import math
class Sudoku:
    def __init__(self, p):
        self.p = p
        self.sqrSz = int(math.sqrt(len(p)))
        
    def solve(self):
        return self.solveCell(0, 0)
    
    def solveCell(self, row, col):
        if col >= len(self.p):
            return True
        elif row >= len(self.p):
            return self.solveCell(0, col+1)
        elif self.p[row][col] != 0:
            return self.solveCell(row+1, col)
        for num in range(1,len(self.p)+1):
            if (self.valid(row, col, num)):
                self.p[row][col] = num
                if self.solveCell(row+1, col):
                    return True
        self.p[row][col]=0
        return False

    def validInRow(self, row, num):
        for col in range(len(self.p)):
            if abs(self.p[row][col]) == num:
                return False 
        return True

    def validInCol(self, col, num):
        for row in range(len(self.p)):
            if abs(self.p[row][col]) == num:
                return False 
        return True
    
    def validInSquare(self, row, col, num):
        r1 = int(row / self.sqrSz) * self.sqrSz
        c1 = int(col / self.sqrSz) * self.sqrSz
        for r in range(r1, (r1+self.sqrSz)):
            for c in range(c1, (c1+self.sqrSz)):
                if abs(self.p[r][c]) == num:
                    return False 
        return True

    def valid(self, row, col, num):
        isValid = self.validInRow(row, num) and self.validInCol(col, num) and self.validInSquare(row, col, num)
        return isValid

    def put(self):
        for row in range(len(self.p)):
            for col in range(len(self.p)):
                print('%-2d' % abs(self.p[row][col]), end="")
            print("")


from time import time

games = load_games()

start = time()

sum_games = 0
for n in range(NGAMES):
    s = Sudoku(games[n])
    print("Puzzle #", n)
    #s.put()
    if s.solve():
        #direct_solve_game(games[n])
        print("")
        print("Solution #", n)
        #s.put()
    else:
        print("Puzzle has no solution.")
    print("")
    print("Time:", time() - start)
    print("")
    sum_games += abs(s.p[0][0]) * 100 + abs(s.p[0][1]) * 10 + abs(s.p[0][2])

print("\nResult:", sum_games)

