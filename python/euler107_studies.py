matrix = [[0,16,12,21,0,0,0],
          [16,0,0,17,20,0,0],
          [12,0,0,28,0,31,0],
          [21,17,28,0,18,19,23],
          [0,20,0,18,0,0,11],
          [0,0,31,19,0,0,27],
          [0,0,0,23,11,27,0]]

usedPath = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]

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
                path = shortestPath(c, b, visited)
                if path != None:
                    weight = calcWeight((a,c)) + calcWeight(path)
                    if minWeight == None or weight < minWeight:
                        minWeight = weight
                        minPath = path
        if minPath == None:
            return None
        else:
            return (a,) + minPath

#print(calcWeight((0,1,4)))
#print(calcWeight((0,3,4)))
#print(calcWeight((0,2,3,4)))

def calcAllPaths():
    for a in range(len(matrix)):
        for b in range(a+1, len(matrix)):
            path = shortestPath(a, b)
            markUsed(path)

def removeLeastPaths():
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            if usedPath[a][b] == 1:
                matrix[a][b] = 0
    #clear used matrix
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            usedPath[a][b] = 0



#print(shortestPath(0,6))
print(calcNetWeight())

calcAllPaths()

##matrix[0][3] = 0
##matrix[3][0] = 0
##matrix[2][3] = 0
##matrix[3][2] = 0
##matrix[3][6] = 0
##matrix[6][3] = 0
##matrix[5][6] = 0
##matrix[6][5] = 0
##matrix[2][5] = 0
##matrix[5][2] = 0
##matrix[2][5] = 0
##matrix[5][2] = 0
##matrix[1][4] = 0
##matrix[4][1] = 0

#print(calcNetWeight())
