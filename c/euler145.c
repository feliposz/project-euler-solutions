/*
Problem 145
16 March 2007

Some positive integers n have the property that the sum [ n +
reverse(n) ] consists entirely of odd (decimal) digits. For instance,
36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers
reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are
not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10**9)?

Runned in 233 seconds
*/

#include <stdio.h>
#include <time.h>


long reverseNum(long num)
{
    long rev = 0;

    while (num) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }

    return rev;
}

int isReversible(int num)
{
    long sum, digit;

    if (num % 10 == 0) {
        return 0;
    }

    sum = num + reverseNum(num);
    while (sum) {
        digit = sum % 10;
        if (!(digit & 1)) {
            return 0;
        }
        sum /= 10;
    }

    return 1;
}

int main()
{
    long num, count = 0;
    time_t start = time(NULL);

    for (num = 1; num < 1000000000; num++) {
        if (isReversible(num)) {
            count++;
        }
    }
    printf("Count = %ld, Time = %ld", count, time(NULL) - start);

    return 0;
}
