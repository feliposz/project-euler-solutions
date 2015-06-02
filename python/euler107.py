##matrix = [[0,16,12,21,0,0,0],
##          [16,0,0,17,20,0,0],
##          [12,0,0,28,0,31,0],
##          [21,17,28,0,18,19,23],
##          [0,20,0,18,0,0,11],
##          [0,0,31,19,0,0,27],
##          [0,0,0,23,11,27,0]]

matrix = []
file = open("network.txt")
while True:
    line = file.readline()
    if not line:
        break
    matrix.append(list(map(int, line.replace("-","0").strip().split(","))))
file.close()
assert len(matrix) == 40 and len(matrix[0]) == 40, "Matrix loaded should be 40x40"

nodesVisited = {}

def dfsTraverse(start, prevVisited=[]):
    nodesVisited[start] = True
    nextVisited = list(prevVisited)
    nextVisited.append(start)
    for next in range(len(matrix)):
        if (matrix[start][next] != 0) and (next not in nextVisited):
            nextVisited.append(next)
    for next in range(len(matrix)):
        if (matrix[start][next] != 0) and (next not in prevVisited):
            dfsTraverse(next, nextVisited)

def isNetConnected():
    global nodesVisited
    nodesVisited = {}
    dfsTraverse(0)
    return len(nodesVisited) == len(matrix)

def calcNetWeight():
    total = 0
    minWeight = None
    maxWeight = None
    for a in range(len(matrix)):
        for b in range(a+1, len(matrix)):
            weight = matrix[a][b]
            if minWeight == None or weight < minWeight:
                minWeight = weight
            if maxWeight == None or weight > maxWeight:
                maxWeight = weight
            total += weight
    return total

def findHeaviestEdge():
    weight = 0
    for a in range(len(matrix)):
        for b in range(a+1, len(matrix)):
            if matrix[a][b] > weight:
                weight = matrix[a][b]
                pair = (a,b)
    return (weight,) + pair

def cleanupNet():
    while True:
        weight, a, b = findHeaviestEdge()
        matrix[a][b] = matrix[b][a] = 0
        if isNetConnected():
            print("Removed {0} to {1} = {2} (Current Weight = {3})".format(a,b,weight,calcNetWeight()))
        else:
            print("Couldn't remove {0} to {1} = {2}".format(a,b,weight))
            print("Stopping.")
            matrix[a][b] = matrix[b][a] = weight
            break



print(calcNetWeight())
cleanupNet()
print(calcNetWeight())
