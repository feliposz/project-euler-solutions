// TODO: need to test this again...

#include<iostream>

using namespace std;

int main() {
	//long num = 13195;
	long long num = 600851475143LL;
	long f = 2, last = 0;
	
	while (num > 1) {
		if (num % f == 0) {
			cout << "Divisible by f: " << f << " num: " << num << '\n';
			while (num % f == 0 && num != f) {
				num /= f;
			}
			last = f;
		}
		f++;
	}
	cout << "Largest factor: " << last << '\n';
}