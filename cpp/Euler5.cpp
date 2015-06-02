#include<iostream>

using namespace std;

long long factorial(int max)
{
    long long num = 1;
    for (int factor = 1; factor <= max; factor++) {
        num *= factor;
    }
    return num;
}

// check if num is divisible by all numbers from 2 to max
bool divisibleByAll(long long num, int max)
{
    for (int divisor = 2; divisor <= max; divisor++) {
        if ((num % divisor) != 0) {
            return false;
        }
    }
    return true;
}

long long solveEuler5(int max_factor)
{
    // first find the product of all the numbers from 1 to 20 (i.e. 20!)
    long long num = factorial(max_factor);

    // then try to reduce it by dividing by the factors as many times as possible
    for (int factor = 2; factor <= max_factor; factor++) {
        // divide as much as possible...
        while (divisibleByAll(num, max_factor)) {
            num /= factor;
        }
        num *= factor; // ...then go back one step
    }

    return num;
}

int main()
{
    //actually this won't work for anything larger than 20 =(
    const int MAX_FACTOR = 20;

    cout << solveEuler5(MAX_FACTOR) << '\n';
    return 0;
}
