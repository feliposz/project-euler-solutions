"""Problem 83
19 November 2004

NOTE: This problem is a significantly more challenging version of
Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to
the bottom right, by moving left, right, up, and down, is indicated in
bold red and is equal to 2297.


131*	673	234*	103*	18*
201*	96*	342*	965	150*
630	803	746	422*	111*
537	699	497	121*	956
805	732	524	37*	331*

Find the minimal path sum, in matrix.txt (right click and 'Save
Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by moving left, right, up, and
down.
"""
from pprint import pprint
from eulerlib import timedRun

# NOTE: check also euler83 (dijkstra version)

# Load the number matrix from file

file = open("matrix.txt", "r")
matrix = []
while True:
    line = file.readline()
    if not line:
        break
    matrix.append(list(map(int, line.split(","))))
file.close()

## For Debugging...
##matrix = [
##    [131, 673, 234, 103,  18],
##    [201,  96, 342, 965, 150],
##    [630, 803, 746, 422, 111],
##    [537, 699, 497, 121, 956],
##    [805, 732, 524,  37, 331],
##    ]

rows = len(matrix)
cols = len(matrix[0])

# Check this for details
# http://en.wikipedia.org/wiki/A*_search_algorithm

def neighbor_nodes(current):
    i, j = current
    assert i >= 0 and i <= rows, "Invalid row"
    assert j >= 0 and j <= cols, "Invalid column"
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j)) # up
    if i < rows - 1:
        neighbors.append((i + 1, j)) # down
    if j > 0:
        neighbors.append((i, j - 1)) # left
    if j < cols - 1:
        neighbors.append((i, j + 1)) # right
    return neighbors

def dist_between(current, neighbor):
    assert current != neighbor, "Shouldn't be the same"
    i, j = neighbor
    m, n = current
    return matrix[i][j] + matrix[m][n]

def lowest_value(keys, scores):
    assert len(keys) > 0, "Empty keyset"
    assert len(scores) > 0, "Empty scoreset"
    low_key = list(keys)[0]
    low_val = scores[low_key]
    for k in keys:
        if scores[k] < low_val:
            low_key = k
            low_val = scores[k]
    return low_key


# Returning 0 should makes this behave just like Dijkstra's algorithm

def heuristic_score_estimate(start, goal):
#    i, j = start
#    m, n = goal
#    return abs(m-i) + abs(n-j)
    return 0
        
def a_star(start, goal):
    closed_set = []
    open_set = [start]
    came_from = {}

    g_score = {start: 0}
    h_score = {start: heuristic_score_estimate(start, goal)}
    f_score = {start: g_score[start] + h_score[start]}

    while len(open_set) > 0:
        current = lowest_value(open_set, f_score)
        if current == goal:
            #return reconstruct_path(came_from, came_from[goal])
            return reconstruct_path(came_from, goal)

        open_set.remove(current)
        closed_set.append(current)

        for neighbor in neighbor_nodes(current):
            if neighbor in closed_set:
                continue
            tentative_g_score = g_score[current] + dist_between(current, neighbor)

            if neighbor not in open_set:
                open_set.append(neighbor)
                h_score[neighbor] = heuristic_score_estimate(neighbor, goal)
                tentative_is_better = True
            elif tentative_g_score < g_score[neighbor]:
                tentative_is_better = True
            else:
                tentative_is_better = False

            if tentative_is_better:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h_score[neighbor]

    return None

def reconstruct_path(came_from, target):
    if target in came_from:
        p = reconstruct_path(came_from, came_from[target])
        return p + [target]
    else:
        return [target]

def euler83_astart():
    start = (0, 0)
    goal = (rows - 1, cols - 1)
    path = a_star(start, goal)

    total = 0
    for node in path:
        i, j = node
        val = matrix[i][j]
        print("node = %d,%d / value = %d" % (i, j, val))
        total += val
    print(total)
    #425185

if __name__ == "__main__":
    timedRun(euler83_astart)
