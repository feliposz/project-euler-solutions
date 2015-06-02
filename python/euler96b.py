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


# NOTE: This code is a mess, also it's terribly inefficient! I guess
# it's not even working for most cases, except for direct_solve_game()
# that is simple and works.

# Try to do something simpler as http://norvig.com/sudoku.html

from copy import deepcopy

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
                games[game][row].append(s[col])
    return games

def print_game(game):
    max_len = 0
    for row in game:
        for col in row:
            if len(col) > max_len:
                max_len = len(col)

    max_len += 1

    for i in range(9):
        if i != 0 and i % 3 == 0:
            print("-" * (max_len * 9))
        for j in range(9):
            if j != 0 and j % 3 == 0:
                print("|", end="")
            s = (game[i][j]+ (" " * max_len))[:max_len]
            print(s, end="")
        print("")


def transfer_solution(game, alt_game):
    for i in range(9):
        for j in range(9):
            game[i][j] = alt_game[i][j]

def direct_solve_game(game):
    while True:
        changed = False
        for i in range(9):
            for j in range(9):
                if solve_cell(i, j, game):
                    changed = True
        if not changed:
            break
    
    for i in range(9):
        for j in range(9):
            if len(game[i][j]) != 1:
                return False
    return True

def solve_cell(row, col, game):
    if game[row][col] != "0" and len(game[row][col]) == 1:
        return False
    
    available = "123456789"
    
    # check same column
    for i in range(9):
        if len(game[i][col]) == 1 and game[i][col] in available:
            available = available.replace(game[i][col], "")
            
    # check same row
    for j in range(9):
        if len(game[row][j]) == 1 and game[row][j] in available:
            available = available.replace(game[row][j], "")
            
    # check same quadrant
    bi = row // 3 * 3
    bj = col // 3 * 3
    for i in range(bi, bi+3):
        for j in range(bj, bj+3):
            if len(game[i][j]) == 1 and game[i][j] in available:
                available = available.replace(game[i][j], "")

    # only one possibility - direct solution
    game[row][col] = available
    if len(available) == 1:
        return True
    else:
        return False

def try_solve(game, depth = 0):
    #print(depth)
    if direct_solve_game(game):
        return True

    # list possible alternatives
    try_cells = []
    for i in range(9):
        for j in range(9):
            if len(game[i][j]) != 1:
                try_cells.append((game[i][j], i, j))

    # sort by smallest number of alternatives first
    try_cells = sorted(try_cells, key=lambda e: len(e[0]))

##    print_game(game)
##    print(try_cells[:10])
##    exit(0)

    for cell in try_cells:
        #if depth == 0:
        #    print(try_cells)
        alternatives, i, j = cell
        alt_game = deepcopy(game)
        for a in alternatives:
            alt_game[i][j] = a
            if try_solve(alt_game, depth + 1):
                #print_game(alt_game)
                transfer_solution(game, alt_game)
                #exit(0)
                #print(depth)
                return True

    return False
    

def collisions(game):
    collision_set = set([])
    # check collisions in row
    for i in range(9):
        for j1 in range(9):
            for j2 in range(j1, 9):
                if j1 != j2 and game[i][j1] == game[i][j2]:
                    collision_set.add((i, j1))
                    collision_set.add((i, j2))

    # check collisions in column
    for j in range(9):
        for i1 in range(9):
            for i2 in range(i1, 9):
                if i1 != i2 and game[i1][j] == game[i2][j]:
                    collision_set.add((i1, j))
                    collision_set.add((i2, j))
            
    # check same quadrant
    # (this is producing duplicate counts, but maybe that's not important)
    for i1 in range(9):
        for j1 in range(9):
            bi = i1 // 3 * 3
            bj = j1 // 3 * 3
            for i2 in range(bi, bi+3):
                for j2 in range(bj, bj+3):
                    if (i1 != i2 or j1 != j2) and game[i1][j1] == game[i2][j2]:
                        collision_set.add((i1, j1))
                        collision_set.add((i2, j2))
    return list(collision_set)
   
# TODO: solve problems with no direct solution   

from time import time

games = load_games()

start = time()

sum_games = 0
for n in range(NGAMES):
    print("Puzzle #", n)
    print_game(games[n])
    try_solve(games[n])
    #direct_solve_game(games[n])
    print("")
    print("Solution #", n)
    print_game(games[n])
    print("")
    print("Time:", time() - start)
    print("")   
    sum_games += int("".join(games[n][0][0:3]))

print("\nResult:", sum_games)
##n = 20
##print("Before")
##print_game(games[n])
##
##print("Solving")
###direct_solve_game(games[n])
##solved = try_solve(games[n])
##print("Status solved?", solved)
##
##print("Solved")
##print_game(games[n])
