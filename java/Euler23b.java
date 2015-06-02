/*
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
*/

import java.util.*;

// took < 3 seconds!!!

class Euler23b {

	private static final int MAX = 28123;

	private static int sumOfDivisors(int n) {
		int sum = 0;
		for (int i = 1; i <= n/2; i++) {
			if (n % i == 0)
				sum += i;
		}
		return sum;
	}
	
	public static void main(String[] args) {
		
		ArrayList<Integer> abundant = new ArrayList<Integer>();
	
		System.out.print("Creating list of abundants...");
		for (int num = 1; num < MAX; num++) {
			int sod = sumOfDivisors(num);
			if (sod >num)
				abundant.add(num);
		}
		System.out.println("done.");

		System.out.println("abundants = " + abundant.size());
		
		System.out.print("Creating table of representable numbers...");
		boolean representable[] = new boolean[MAX];
		for (int i = 0; i < abundant.size(); i++) {
			for (int j = i; j < abundant.size(); j++) {
				int num = abundant.get(i) + abundant.get(j);
				if (num < MAX)
					representable[num] = true;
			}
		}
		System.out.println("done.");

		System.out.print("Adding non-representable...");
		long sumOfNonRepresentable = 0;
		for (int num = 1; num < MAX; num++) {
			if (!representable[num])
				sumOfNonRepresentable += num;
		}
		System.out.println("done.");

		System.out.println("Sum of Non-Representable: " + sumOfNonRepresentable);
	}

}