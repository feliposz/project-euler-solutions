#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
//#define LIMIT 100000
 #define LIMIT 100000000
#define PLIMIT (LIMIT + 2)


//unsigned char primes[PLIMIT];
unsigned char *primes;

void generatePrimesSieve()
{
    long long i, j;

    primes = (unsigned char*) malloc(PLIMIT * sizeof(unsigned char));

    printf("addr = %p\n", primes);

    if (primes == NULL) {
        exit(1);
    }

    primes[0] = 0;
    primes[1] = 0;
    for (i = 2; i < PLIMIT; i++) {
        primes[i] = 1;
    }

    for (i = 2; i < PLIMIT; i++) {
        if (primes[i]) {
            for (j = i+i; j > 0 && j < PLIMIT; j+=i) {
                primes[j] = 0;
            }
        }
    }

}

// TODO: maybe other improvements...
int isPrimeGeneratingInteger(int n)
{
    int d, nd, x;
    int lastDigit = n % 10;
    if ((n > 10) && (lastDigit != 0) && (lastDigit != 2) && (lastDigit != 8)) {
        return 0;
    }
    int sq = sqrt(n);
    for (d = 1; d <= sq; d++) {
        if (n % d != 0) {
            continue;
        }
        nd = n / d;
        if (d > nd) {
            break;
        }
        x = d + n / d;
        //printf("%d + %d / %d = %d + %d = %d\n", d, n, d, d, n / d, x);
        if (!primes[x]) {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int i;
    long long total = 0;

    printf("Generating primes:");
    generatePrimesSieve();
    printf("done.\n");

    for (i = 1; i <= LIMIT; i++) {
        if (isPrimeGeneratingInteger(i)) {
            total = total + (long long) i;
            //printf("pgi:  %d - total: %lld\n", i, total);
        }
    }

    printf("solution: %lld\n", total);

    return 0;
}
