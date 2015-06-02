#Almost equilateral triangles
#Problem 94
#It is easily proved that no equilateral triangle exists with integral length
#sides and integral area. However, the almost equilateral triangle 5-5-6 has an
# area of 12 square units.
#
#We shall define an almost equilateral triangle to be a triangle for which two
#sides are equal and the third differs by no more than one unit.
#
#Find the sum of the perimeters of all almost equilateral triangles with integral
#side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

#x = equal sides, y = different side

import math

def isPerfectSquare(n):
    x = int(math.sqrt(n))
    return x * x == n

def isAlmostIsosceles(x, y):
    #a = math.sqrt(y*y * (x*x - y*y/4) / 4)
    #a2 = y*y * (x*x - y*y/4) / 4
    #a2times4 = y*y * (x*x - y*y/4)
    a2times16 = y*y * (4*x*x - y*y)
    if a2times16 % 16 != 0:
        return False
    a2 = a2times16 // 16
    return isPerfectSquare(a2)

def euler94(n):
    sum = 0
    i = 5
    while i <= n:
        if isAlmostIsosceles(i, i - 1):
            print (i, i, i-1, sum)
            p = 3 * i - 1
            sum += p
            if i <= 100:
                i *= 3
            elif i <= 10000:
                i = int(i * 3.7)
            elif i <= 1000000:
                i = int(i * 3.732)
            else:
                i = int(i * 3.73205)
        if isAlmostIsosceles(i, i + 1):
            print (i, i, i+1, sum)
            p = 3 * i + 1
            sum += p
            if i <= 100:
                i *= 3
            elif i <= 10000:
                i = int(i * 3.7)
            elif i <= 1000000:
                i = int(i * 3.732)
            else:
                i = int(i * 3.73205)
        i += 1
    return sum

#print(isAlmostIsosceles(5,6))

#print(euler94(333333333))

print(euler94(100000000000))
