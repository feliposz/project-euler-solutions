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


# NOTE: Strange thing that I did here, trying to solve by "randomly"
# assigning digits and swapping them. Bad idea. I got lost in the code
# and couldn't find my way out of it.

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
                games[game][row].append(int(s[col]))
    return games

def print_game(game):
    for row in game:
        for col in row:
            print(col, " ", end="")
        print("")


def fixed_copy(game):
    fixed = [[game[i][j] != 0 for j in range(len(game[i]))] for i in range(len(game))]
    alt = [[game[i][j]  for j in range(len(game[i]))] for i in range(len(game))]
##    for i in range(len(game)):
##        for j in range(len(game[i])):
##            fixed[i][j] = game[i][j] != 0
##            alt[i][j] = game[i][j]
    return fixed, alt


def transfer_solution(game, alt_game):
    for i in range(len(game)):
        for j in range(len(game[i])):
            game[i][j] = alt_game[i][j]


def direct_solve_game(game):
    while True:
        changed = False
        for i in range(len(game)):
            for j in range(len(game[i])):
                if solve_cell(i, j, game):
                    changed = True
        if not changed:
            break
    
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == 0:
                return False
    return True

def solve_cell(row, col, game):
    if game[row][col] != 0:
        return False
    
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # check same column
    for i in range(9):
        if game[i][col] in available:
            available.remove(game[i][col])
            
    # check same row
    for j in range(9):
        if game[row][j] in available:
            available.remove(game[row][j])
            
    # check same quadrant
    bi = row // 3 * 3
    bj = col // 3 * 3
    for i in range(bi, bi+3):
        for j in range(bj, bj+3):
            if game[i][j] in available:
                available.remove(game[i][j])

    # only one possibility - direct solution
    if len(available) == 1:
        game[row][col] = available[0]
        return True
    else:
        return False

def try_solve(game, level=1):
    #print(level)
    if solve_game(game):
        return True
    fixed, alt = fixed_copy(game)


    # while there are colisions
    # swap positions

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

from random import randint

def crazy_swap(fixed, alt):
    while True:
        i1 = randint(0, 8)
        j1 = randint(0, 8)
        if not fixed[i1][j1]:
            break
    while True:
        i2 = randint(0, 8)
        j2 = randint(0, 8)
        if alt[i1][j1] != alt[i2][j2]:
            break
    alt[i1][i1], alt[i2][j2] = alt[i2][j2], alt[i1][i1]
    return i1, i2, j1, j2
        
def random_swap(fixed, alt, collision_list):
    filtered = []
    for c in collision_list:
        i, j = c
        if not fixed[i][j]:
            filtered.append(c)

    # find a colliding cell that is not a fixed cell
    i1, j1 = filtered[randint(0, len(filtered) - 1)]

    # filter only other collisions in same row/cell/quadrant
    filtered2 = []
    for c in filtered:
        fi, fj = c
        if (fi == i1 and fj == j1) or (alt[fi][fj] == alt[i1][j1]):
            pass # same cell or same value, pass
        elif fi == i1:
            filtered2.append(c) # same row
        elif fj == i1:
            filtered2.append(c) # same column
        elif fi // 3 == i1 // 3 and fj // 3 == j1 // 3:
            filtered2.append(c) # same quadrant

    # Try to swap with another colliding cell
    if randint(0, 1) == 0 and len(filtered2) > 0:
        i2, j2 = filtered2[randint(0, len(filtered2) - 1)]
    else:
        while True:
            # pick what to swap
            what = randint(1, 3)
            if what == 1: # same row
                i2 = i1
                j2 = randint(0, 8)
            elif what == 2: # same column
                i2 = randint(0, 8)
                j2 = j1
            elif what == 3: # same quadrant
                i2 = i1 // 3 * 3 + randint(0, 2)
                j2 = j1 // 3 * 3 + randint(0, 2)
            if not fixed[i2][j2] and (i1 != i2 or j1 != j2):
                break

    alt[i1][i1], alt[i2][j2] = alt[i2][j2], alt[i1][i1]
    return i1, i2, j1, j2

def undo_swap(alt, swapped_cells):
    i1, i2, j1, j2 = swapped_cells
    alt[i1][i1], alt[i2][j2] = alt[i2][j2], alt[i1][i1]
    
# TODO: solve problems with no direct solution   

games = load_games()

##for i in range(NGAMES):
##    solve_game(games[i])
##    print(i, games[i][0][0:3])

n = 1
print("Before")
print_game(games[n])
##print("Solving")
##print(try_solve(games[n]))
###solve_game(games[1], True)
##print("After")
##print_game(games[n])

fixed, alt = fixed_copy(games[n])

# fill non-fixed position with missing values in the same row
for i in range(9):
    n = 1
    for j in range(9):
        if alt[i][j] == 0:
            while n in alt[i]:
                n += 1
            alt[i][j] = n

print("Dummy")
print_game(alt)

print("Solving")
# while there are colisions
collisions_list = collisions(alt)
count = len(collisions_list)
previous = count
while count > 0:
    #swapped_cells = random_swap(fixed, alt, collisions_list)
    swapped_cells = crazy_swap(fixed, alt)
    collisions_list = collisions(alt)
    count = len(collisions_list)
    if count > previous:
        undo_swap(alt, swapped_cells)
        continue
    if count < previous:
        print(count)
    previous = count
    
print("Solved")
print_game(alt)
