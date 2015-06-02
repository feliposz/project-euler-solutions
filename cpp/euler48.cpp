#include<iostream>
using namespace std;

long long power(int b, int e) {
    long long res = 1;
    for (int i=0; i<e && res!=0; i++) {
        res = res * b % 10000000000LL;
    }
    return res;
}

int main() {
    long long result = 0;
    for (int i=1; i<1001;i++)
        result += power(i, i);
    cout << result % 10000000000LL << endl;
}
