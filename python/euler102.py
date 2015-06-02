from eulerlib import triangleArea, pointInTriangle

def euler102():
    """Solve problem 102 from Project Euler."""
    count = 0
    origin = (0, 0)
    file = open("triangles.txt")
    while True:
        line = file.readline()
        if not line:
            break
        trianglePoints = tuple(map(int, line.split(",")))
        if pointInTriangle(origin, trianglePoints):
            count += 1
    file.close()
    print("Triangles containing the origin =", count)

if __name__ == "__main__":
    euler102()



    
