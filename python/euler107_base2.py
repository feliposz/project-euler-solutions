matrix = [[0,16,12,21,0,0,0],
          [16,0,0,17,20,0,0],
          [12,0,0,28,0,31,0],
          [21,17,28,0,18,19,23],
          [0,20,0,18,0,0,11],
          [0,0,31,19,0,0,27],
          [0,0,0,23,11,27,0]]

matrix = []
file = open("network.txt")
while True:
    line = file.readline()
    if not line:
        break
    matrix.append(list(map(int, line.replace("-","0").strip().split(","))))
file.close()

assert len(matrix) == 40 and len(matrix[0]) == 40, "Matrix loaded should be 40x40"

usedPath = [[0 for x in range(len(matrix))] for x in range(len(matrix))]

def calcWeight(path):
    i = 0
    j = 1
    weight = 0
    while j < len(path):
        a = path[i]
        b = path[j]
        #print("from",a,"to",b,"weight",matrix[a][b])
        weight += matrix[a][b]
        i += 1
        j += 1
    return weight

def markUsed(path):
    i = 0
    j = 1
    weight = 0
    while j < len(path):
        a = path[i]
        b = path[j]
        usedPath[a][b] += 1
        usedPath[b][a] += 1
        i += 1
        j += 1


def calcNetWeight():
    weight = 0
    for a in range(len(matrix)):
        for b in range(a+1, len(matrix)):
            weight += matrix[a][b]
    return weight

def shortestPath(a,b,visited=[]):
    connections = matrix[a]
    if connections[b] != 0:
        return (a,b)
    else:
        minPath = None
        minWeight = None
        visited.insert(0,a)
        for c in range(len(connections)):
            if connections[c] != 0 and not c in visited:
                path = shortestPath(c, b, list(visited))
                if path != None:
                    weight = calcWeight((a,c)) + calcWeight(path)
                    if minWeight == None or weight < minWeight:
                        minWeight = weight
                        minPath = path
        if minPath == None:
            return None
        else:
            return (a,) + minPath


def removeUnusedPaths():
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            if usedPath[a][b] == 0:
                if matrix[a][b] != 0:
                    print("Removing {0} to {1}".format(a,b))
                    matrix[a][b] = 0

    #clear used matrix
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            usedPath[a][b] = 0

def checkAllPaths():
    for a in range(len(matrix)):
        for b in range(a+1, len(matrix)):
            path = shortestPath(a, b)
            markUsed(path)

def isNetConnected():
    a = 0
    for b in range(1, len(matrix)):
        path = shortestPath(a,b)
        if path == None:
            print("No path from {0} to {1}".format(a,b))
            return False
    return True

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
            print("Removed {0} to {1} = {2}".format(a,b,weight))
        else:
            print("Couldn't remove {0} to {1} = {2}".format(a,b,weight))
            print("Stopping.")
            matrix[a][b] = matrix[b][a] = weight
            break



#print(calcNetWeight())
#cleanupNet()
#shortestPath(0,6)
#print(calcNetWeight())
