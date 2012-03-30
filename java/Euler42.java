/*
http://projecteuler.net/problem=42

Problem 42
25 April 2003

The nth term of the sequence of triangle numbers is given by
 tn = ½n(n+1); so the first ten triangle numbers are:

1
 3
 6
 10
 15
 21
 28
 36
 45
 55
 ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example
 the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...')
 a 16K text file containing nearly two-thousand common English words
 how many are triangle words?
*/

import java.io.*;
import java.util.*;

class Euler42 {

	private static int calcValue(String name) {
		int total = 0;
		for (int i = 0; i < name.length(); i++) {
			total += name.charAt(i) - 'A' + 1;
		}
		return total;
	}
	
	private static int triangleNum(int n) {
		return n * (n + 1) / 2;
	}
	
	private static boolean isTriangleNumber(int num) {
		for (int i = 1; ; i++) {
			int t = triangleNum(i);
			if (t == num)
				return true;
			if (t > num)
				return false;
		}		
	}

	public static void main(String[] args) throws IOException {
		BufferedReader rd = new BufferedReader(new FileReader("words.txt"));
		String[] nameArray = rd.readLine().replace("\"", "").split(",");
		int count = 0;
		for (int i = 0; i < nameArray.length; i++) {
			if (isTriangleNumber(calcValue(nameArray[i]))) {
				System.out.println(nameArray[i] + " " + calcValue(nameArray[i]));
				count++;
			}
		}
		System.out.println("");
		System.out.println("Triangle words = " + count);
	}
	
}
