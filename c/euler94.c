#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double isoscelesArea(double x, double y)
{
    double h = sqrt(x*x - y*y/4);
    double b = y;
    double a = b * h / 2.0;
    return a;
}

long long euler94(int n)
{
    long long sum = 0, ant = 0;
    long long i, p;
    for (i = 2; i < n; i++) {
        double a = isoscelesArea(i, i - 1);
        double b = isoscelesArea(i, i + 1);
        if (fabs(floor(a) - a) < 0.000000001) {
            //printf("%d, %d, %d", i, i, i-1)
            p = 3 * i - 1;
            sum += p;
        }
        if (fabs(floor(b) - b) < 0.000000001) {
            //printf("%d, %d, %d", i, i, i+1)
            p = 3 * i + 1;
            sum += p;
        }
        if (sum < ant) {
            printf("overflow:\nant = %lld\nsum = %lld\n", ant,sum);
            exit (1);
        }
        ant = sum;
    }
    return sum;
}

int main()
{
    //printf("Result: %ll\n", );
    long long x = euler94(333333334);
    printf("%lld\n", x);
    return 0;
}
