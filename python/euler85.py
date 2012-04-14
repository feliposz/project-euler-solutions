"""Problem 85
17 December 2004

By counting carefully it can be seen that a rectangular grid measuring
3 by 2 contains eighteen rectangles:

 ___ ___ ___    ___ ___ ___    ___ ___ ___
|###|   |   |  |###|###|   |  |###|###|###|
|###|___|___|  |###|###|___|  |###|###|###|
|   |   |   |  |   |   |   |  |   |   |   |
|___|___|___|  |___|___|___|  |___|___|___|
      6              4              2

 ___ ___ ___    ___ ___ ___    ___ ___ ___
|###|   |   |  |###|###|   |  |###|###|###|
|###|___|___|  |###|###|___|  |###|###|###|
|###|   |   |  |###|###|   |  |###|###|###|
|###|___|___|  |###|###|___|  |###|###|###|
      3              2              1

Although there exists no rectangular grid that contains exactly two
million rectangles, find the area of the grid with the nearest
solution.
"""

from eulerlib import timedRun

# Check fast version below
def SLOW_countRectsInGrid(gridWidth, gridHeight, abortLimit=None):
    """Count how many rectangles fit in a grid with given dimensions.

    'abortLimit' is an optional argument to avoid counting beyond a
    certain limit."""
    
    count = 0
    for width in range(1, gridWidth + 1):
        for height in range(1, gridHeight + 1):
            instances = ((gridWidth - width + 1) * (gridHeight - height + 1))
            #print("rectangle of %d by %d has %d instances" % (w, h, instances))
            count += instances
            if abortLimit and count > abortLimit:
                return 0
    return count

# This much faster solution was found at:
# http://projecteuler.net/thread=85
def countRectsInGrid(gridWidth, gridHeight, abortLimit=None):
    """Count how many rectangles fit in a grid with given dimensions.

    'abortLimit' is an optional argument to avoid counting beyond a
    certain limit."""

    return gridWidth * (gridWidth + 1) * gridHeight * (gridHeight + 1) // 4

def euler85():
    """Solves problem 85 from Project Euler."""
    # countRectsInGrid(1, 2000) is already 2001000, no need to check
    # above this limit.
    LIMIT = 2000
    GOAL = 2000000

    # Start with a know closest value
    closestDif = abs(GOAL - countRectsInGrid(1, 2000))
    closestDim = (0, 0)
    closestArea = 0
    
    for gridWidth in range(2, LIMIT):
        for gridHeight in range(2, gridWidth):
            
            #count = SLOW_countRectsInGrid(gridWidth, gridHeight, GOAL + closestDif)
            count = countRectsInGrid(gridWidth, gridHeight, GOAL + closestDif)
            dif = abs(GOAL - count)

            # Found a better match
            if dif < closestDif:
                closestDif = dif
                closestDim = (gridWidth, gridHeight)
                closestArea = gridWidth * gridHeight
                print("Closest so far: dim =", closestDim,
                      " area =", closestArea, " count =", count)

# Tests
assert countRectsInGrid(3, 2) == 18, "A 3 by 2 grid should have 18 rectangles."

if __name__ == "__main__":
    timedRun(euler85)

