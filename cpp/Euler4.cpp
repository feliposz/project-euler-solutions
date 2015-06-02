// Project Euler - Problem 4 solution in C++

#include<iostream>
#include<ctime>
using namespace std;

// NOTE: the multiplication of numbers larger than 4 digits could lead to
//       products bigger than 2 billion (needs to use 64-bit type!)

// OBS: the original problem asks for only 3 digits (a 32-bit int would suffice)
//      i.e. a long or an int (in a 32-bit compiler/architecture)

const long long MIN = 10000;
const long long MAX = 99999;

long long reverse(long number)
{
	int reversed = 0;
	while (number > 0) {
		reversed = reversed * 10 + number % 10;
		number /= 10;
	}
	return reversed;
}

bool isPalindrome(long long number)
{
	return number == reverse(number);
}

int main(int argc, char* argv[])
{
	int max = 0;

	for (long long i = MAX; i >= MIN; i--) { // reversed the order
		for (long long j = i; j >= MIN; j--) { // j = i halves the number of calculations needed!
			long long product = i * j;
			if (product <= max) // since the order is reversed
				break;          // break when found a product smaller for the current j
			if (isPalindrome(product)) {
				max = product;
				cout << "Found a bigger palindrome: " << i << " * " << j;
				cout << " = " << product << " (time: " << time(NULL) << ")\n";
			}
		}
	}
	cout << "Biggest found: " << max << '\n';
	cin.get();
	return 0;
}
