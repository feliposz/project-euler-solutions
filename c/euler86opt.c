#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int euler86(n)
{
    int count = 0;
    long w = 1, h, l;
    long pathSq, path;

    while (1) {
        for (h = 1; h <= w; h++) {
            for (l = 1; l <= h; l++) {
                long pathSq = (l+h) * (l+h) + w * w;
                long path = sqrt(pathSq);
                if (path*path == pathSq) {
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
