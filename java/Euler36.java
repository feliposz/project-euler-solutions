/*
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
*/

class Euler36 {

	private static int reverseNum(int num) {
		int reverse = 0;
		while (num > 0) {
			reverse = reverse * 10 + num % 10;
			num /= 10;
		}
		return reverse;
	}
	
	private static boolean isPalindrome(int num) {
		return num == reverseNum(num);
	}

	private static int reverseBits(int num) {
		int reverse = 0;
		while (num > 0) {
			reverse = reverse * 2 + num % 2;
			num /= 2;
		}
		return reverse;		
	}
	
	private static boolean isBitPalindrome(int num) {
		return num == reverseBits(num);
	}
	
	private static String bitToString(int num) {
		String s = "";
		while (num > 0) {
			s = (num % 2) + s;
			num /= 2;
		}
		return s;
	}
	
	public static void main(String[] args) {
		int sum = 0;
		for (int i = 1; i < 1000000; i++) {
			if (isPalindrome(i) && isBitPalindrome(i)) {
				sum += i;
				System.out.format("%d %s\n", i, bitToString(i));
			}
		}
		System.out.println("Sum = " + sum);
	}

}