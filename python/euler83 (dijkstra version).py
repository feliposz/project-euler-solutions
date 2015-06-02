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

# NOTE: check also euler83 (a-start version)

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

INFINITY = 999999999

# Adapted from:
# http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

def neighbor_nodes(current):
    """Returns valid neighbor nodes (up, down, left, right) in the
    matrix."""    
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
    """Returns the distance between current node and it's neighbor."""
    assert neighbor in neighbor_nodes(current), "Should be a beighbor."
    i, j = neighbor
    m, n = current
    return matrix[i][j] + matrix[m][n]

def smallest_distance(vertexes, dist):
    """Returns the smallest distance in dist where key is in vertexes."""
    smallest_k = vertexes[0]
    smallest_d = dist[smallest_k]
    for v in vertexes:
        if dist[v] < smallest_d:
            smallest_d = dist[v]
            smallest_k = v
    return smallest_k

def shortest_path(vertexes, source, target):
    """Returns the shortest path between source and target."""
    dist = {}
    previous = {}
    for v in vertexes:
        dist[v] = INFINITY
        previous[v] = None

    dist[source] = 0
    open_set = vertexes[:]
    while len(open_set) > 0:
        current = smallest_distance(open_set, dist)
        if dist[current] == INFINITY:
            break
        if current == target:
            return reconstruct_path(previous, current)
        open_set.remove(current)
        for neighbor in neighbor_nodes(current):
            if neighbor in open_set:
                alt = dist[current] + dist_between(current, neighbor)
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    previous[neighbor] = current
                    # decrease position of neighbor in list?
                    # this is the only part that's not really clear for me
                    open_set.remove(neighbor)
                    open_set.insert(0, neighbor) 

    # dijkstra's algorithm return the map of distances (dist)
    # but in my case, I return the shortest path above
    print("At: ", current, " (no path found to target)")
    return None

def reconstruct_path(previous, target):
    """Reconstruct the path going back from target to original node in
    the 'previous' map of nodes."""    
    S = []
    current = target
    while current in previous:
        S = [current] + S
        current = previous[current]
    return S

def euler83_dijkstra():
    vertexes = [(i, j) for i in range(rows) for j in range(cols)]

    start = (0, 0)
    goal = (rows - 1, cols - 1)
    path = shortest_path(vertexes, start, goal)

    assert path != None, "shortest_path() should return a path in this case."

    total = 0
    for node in path:
        i, j = node
        val = matrix[i][j]
        print("node = %d,%d / value = %d" % (i, j, val))
        total += val
    print(total)
    #425185


if __name__ == "__main__":
    timedRun(euler83_dijkstra)
    
