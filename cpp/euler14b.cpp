#include<iostream>
using namespace std;

int count_chain(unsigned long n)
{
    if (n == 1)
        return 1;
    else if (n % 2 == 0)
        return count_chain(n / 2) + 1;
    else
        return count_chain((3 * n + 1)/2) + 2;
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
