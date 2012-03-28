/*
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
*/

// The UGLIEST solution so far... but fast!
// TODO: Should find a way to use recursion excluding 1 element and finding the permutations of the remaining...
// Ex: perm(0123456789) = 0 * perm(123456789) = 1 * perm(23456789) ... 8 * perm(9) = 9 * empty

class Euler24b {

	static final int MAX = 10;

	public static void main(String[] args) {
	
		int count = 0;
		
		for (int a = 0; a < 10; a++) {
		    // and the journey
		    // begins...
			for (int b = 0; b < 10; b++) {
				if (b == a)
					continue;
				for (int c = 0; c < 10; c++) {
					if (c == a || c == b)
						continue;
					for (int d = 0; d < 10; d++) {
						if (d == a || d == b || d == c)
							continue;
						for (int e = 0; e < 10; e++) {
							if (e == a || e == b || e == c || e == d)
								continue;
							for (int f = 0; f < 10; f++) {
								if (f == a || f == b || f == c || f == d || f == e)
									continue;
								for (int g = 0; g < 10; g++) {
									if (g == a || g == b || g == c || g == d || g == e || g == f)
										continue;
									for (int h = 0; h < 10; h++) {
										if (h == a || h == b || h == c || h == d || h == e || h == f || h == g)
											continue;
										for (int i = 0; i < 10; i++) {
											if (i == a || i == b || i == c || i == d || i == e || i == f || i == g || i == h)
												continue;
											for (int j = 0; j < 10; j++) {
												if (j == a || j == b || j == c || j == d || j == e || j == f || j == g || j == h || j == i)
													continue;
												count++;
												if (count == 1000000) {
													System.out.println("Result = "+a+""+b+""+c+""+d+""+e+""+f+""+g+""+h+""+i+""+j);
													return;
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}