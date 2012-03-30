/*
http://projecteuler.net/problem=40

Problem 40
28 March 2003

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part
 find the value of the following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000
*/

class Euler40 {
	public static void main(String[] args) {
		String str = "";
		int pos = 1;
		int n = 0;
		int digit[] = new int[7];
		boolean complete = false; // check if found the last digit
		for (n = 1; !complete; n++) {
			// no need to concatenate the strings
 as long as we keep track of positiong / length
			String s = n + "";
			int len = s.length();
			for (int i = 0; i < len; i++) {
				if (pos + i == 1)
					digit[0] = s.charAt(i) - '0';
				else if (pos + i == 10)
					digit[1] = s.charAt(i) - '0';
				else if (pos + i == 100)
					digit[2] = s.charAt(i) - '0';
				else if (pos + i == 1000)
					digit[3] = s.charAt(i) - '0';
				else if (pos + i == 10000)
					digit[4] = s.charAt(i) - '0';
				else if (pos + i == 100000)
					digit[5] = s.charAt(i) - '0';
				else if (pos + i == 1000000) {
					digit[6] = s.charAt(i) - '0';
					complete = true;
					break;
				}
			}
			pos += len;
		}
		//System.out.println("Last n = " + n);
		
		int product = 1;
		for (int i = 0; i < digit.length; i++) {
			System.out.println("digit[" + i + "] = " + digit[i]);
			product *= digit[i];
		}
		
		System.out.println("Product = " + product);
	}
}