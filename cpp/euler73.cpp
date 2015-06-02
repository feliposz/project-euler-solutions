#include <stdio.h>
#include <time.h>

const int LIMIT = 12000;

int gcd(int a, int b)
{
    int tmp;
    while (b != 0) {
        tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}

int main()
{
    time_t start;
    int den, num;
    long count = 0;
    double fraction;

    start = time(NULL);

    for (den = 2; den <= LIMIT; den++) {
        for (num = 1; num < den; num++) {
            if (gcd(num, den) == 1) {
                fraction = (double) num / (double) den;
                if (fraction > (1.0 / 3.0) && fraction < (1.0 / 2.0)) {
                    count++;
                }
            }
        }
    }

    printf("Count = %ld\n", count);

    printf("Time = %ld\n", time(NULL) - start);

    return 0;
}
