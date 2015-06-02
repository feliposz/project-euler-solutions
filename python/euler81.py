"""Problem 81
22 October 2004

In the 5 by 5 matrix below, the minimal path sum from the top left to
the bottom right, by only moving to the right and down, is indicated
in bold red (*) and is equal to 2427.

131*	673	234	103	18
201*	96*	342*	965	150
630	803	746*	422*	111
537	699	497	121*	956
805	732	524	37*	331*

Find the minimal path sum, in matrix.txt (right click and 'Save
Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
"""

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

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if i == 0 and j == 0: #First element, do nothing
            continue
        elif i == 0: #First row, only add from the left
            matrix[i][j] += matrix[i][j - 1]
        elif j == 0: #First column, only add from above
            matrix[i][j] += matrix[i - 1][j]
        else: #Add the lowest sum from above or from the left
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])
