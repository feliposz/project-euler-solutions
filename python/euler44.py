import math
from eulerlib import pentagonalNum, isPentagonalNum, timedRun

#TODO: There has to be a much faster method for this!
def euler44():
    for i in range(1, 3000):
        for j in range(i, 3000):
            a = pentagonalNum(i)
            b = pentagonalNum(j)
            if isPentagonalNum(a+b) and isPentagonalNum(b-a):
                print("For p[%d] and p[%d], D = %d" % (i, j, b-a))

if __name__ == "__main__":
    timedRun(euler44)

