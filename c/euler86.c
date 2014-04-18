#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
long shortestCuboidPathSq(long w, long h, long l)
{
    long p1sq = (h+l) * (h+l) + w * w;
    long p2sq = (w+h) * (w+h) + l * l;
    long p3sq = (w+l) * (w+l) + h * h;
    if (p1sq < p2sq && p1sq < p2sq) {
        return p1sq;
    } else {
        if (p2sq < p3sq) {
            return p2sq;
        } else {
            return p3sq;
        }
    }
}
*/

// se for garantido que c >= b >= a, o caminho mais curto é (a+b)² + c²
inline long shortestCuboidPathSq(long c, long b, long a)
{
    return (a+b) * (a+b) + c * c;
}


inline int isCuboidPathInteger(int w, int h, int l)
{
    long pathSq = shortestCuboidPathSq(w, h, l);
    long path = sqrt(pathSq);
    return path*path == pathSq; // not the best way to check for perfect square, check: http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
}

int euler86(n)
{
    int count = 0;
    int w = 1, h, l;

    while (1) {
        for (h = 1; h <= w; h++) {
            for (l = 1; l <= h; l++) {
                if (isCuboidPathInteger(w, h, l)) {
                    count++;
                    //printf("%d %d %d %d\n", count, w, h, l);
                    if (count > n) {
                        return w;
                    }
                }
            }
        }
        w++;
    }
}

int main()
{

    printf("Result: %d", euler86(1000000));

    return 0;
}

// < 9sec with full optimization flag (gcc) in (intel i5 3570 - stock)
