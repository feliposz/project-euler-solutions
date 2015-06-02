#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// #define LIMIT 100000000
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

int isPrimeGeneratingInteger(int n)
{
    int d, nd, x;
    int lastDigit = n % 10;
    if ((n > 10) && (lastDigit != 0) && (lastDigit != 2) && (lastDigit != 8)) {
        return 0;
    }
    for (d = 1; d <= n; d++) {
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
            printf("pgi:  %d - total: %lld\n", i, total);
        }
    }

    printf("solution: %lld\n", total);

    return 0;
}


/*
pgi:  99924178 - total: 1736424758361
pgi:  99925498 - total: 1736524683859
pgi:  99928078 - total: 1736624611937
pgi:  99930958 - total: 1736724542895
pgi:  99935922 - total: 1736824478817
pgi:  99936358 - total: 1736924415175
pgi:  99938122 - total: 1737024353297
pgi:  99940198 - total: 1737124293495
pgi:  99940222 - total: 1737224233717
pgi:  99947842 - total: 1737324181559
pgi:  99950302 - total: 1737424131861
pgi:  99959998 - total: 1737524091859
pgi:  99961558 - total: 1737624053417
pgi:  99966262 - total: 1737724019679
pgi:  99972538 - total: 1737823992217
pgi:  99975478 - total: 1737923967695
pgi:  99975838 - total: 1738023943533
pgi:  99978058 - total: 1738123921591
pgi:  99983458 - total: 1738223905049
pgi:  99987262 - total: 1738323892311
pgi:  99989458 - total: 1738423881769
pgi:  99993262 - total: 1738523875031
pgi:  99994078 - total: 1738623869109
pgi:  99994318 - total: 1738723863427
pgi:  99996058 - total: 1738823859485
pgi:  99996670 - total: 1738923856155
pgi:  99996982 - total: 1739023853137
solution: 1739023853137

Process returned 0 (0x0)   execution time : 1736.120 s
Press any key to continue.
*/
