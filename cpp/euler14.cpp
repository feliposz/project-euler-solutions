#include<iostream>
using namespace std;

int count_chain(int i)
{
    long long n = i;
    int count = 1; // the first
    while (n != 1) {
        if (n % 2 == 0)
            n /= 2;
        else
            n = 3*n + 1;
        count++;
    }
    return count;
}

int main()
{
    int longest = 0;

    // just need to test the odd numbers
    for (int i = 1; i < 1000000; i += 2) {
        int size = count_chain(i);
        if (size > longest) {
            longest = size;
            cout << "Longest so far is " << i << " and has " << size << " items."<< endl;
        }
    }

    return 0;
}
