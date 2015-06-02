"""Problem 82
05 November 2004

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any
cell in the left column and finishing in any cell in the right column,
and only moving up, down, and right, is indicated in red and bold; the
sum is equal to 994.


131	673	234*	103*	18*
201*	96*	342*	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331

Find the minimal path sum, in matrix.txt (right click and 'Save
Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
from the left column to the right column.
"""
from pprint import pprint

#--------------------------------------------------------
# Global section

# Load the number matrix from file

file = open("matrix.txt", "r")
matrix = []
while True:
    line = file.readline()
    if not line:
        break
    matrix.append(list(map(int, line.split(","))))
file.close()

#### For Debugging...
##matrix = [
##    [131, 673, 234, 103,  18],
##    [201,  96, 342, 965, 150],
##    [630, 803, 746, 422, 111],
##    [537, 699, 497, 121, 956],
##    [805, 732, 524,  37, 331],
##    ]

# Build a memory to store the intermediary minimal paths
# Actually, only the value on the last column matter in the first round

rows = len(matrix)
cols = len(matrix[0])

memo = []
for row in range(rows):
    memo.append([])
    for col in range(cols):
        memo[row].append(matrix[row][col])

##########################################


# NOTE: All this functinos sum the current value (in matrix) with the
# pre-calculated minimal path in the next column (in memo)

# Find the minimal path sum when moving up
def checkUpAndRight(row, col):
    lowest = checkRight(row, col)
    total = matrix[row][col]
    r2 = row - 1
    while r2 >= 0:
        total += matrix[r2][col]
        if total + memo[r2][col+1] < lowest:
            lowest = total + memo[r2][col+1]
        r2 -= 1
    return lowest

# Find the minimal sum when moving down
def checkDownAndRight(row, col):
    lowest = checkRight(row, col)
    total = matrix[row][col]
    r2 = row + 1
    while r2 < rows:
        total += matrix[r2][col]
        if total + memo[r2][col+1] < lowest:
            lowest = total + memo[r2][col+1]
        r2 += 1
    return lowest

# There is only one possible sum when going to the right
def checkRight(row, col):
    return matrix[row][col] + memo[row][col+1]

# Calculate the minimal path one column at a time
# going from right to left
def buildMemo():
    for col in range(cols - 2, -1, -1):
        for row in range(rows):
            rightSum = checkRight(row, col)
            upSum = checkUpAndRight(row, col)
            downSum = checkDownAndRight(row, col)
            minSum = min(rightSum, upSum, downSum)
            #print(row, col, rightSum, upSum, downSum)
            memo[row][col] = minSum

def euler82():
    buildMemo()
    # The lowest value in the left column is the sum of the lowest path
    lowest = memo[0][0]
    for row in range(rows):
        lowest = min(memo[row][0], lowest)
    print(lowest)

euler82()
