class Euler45b {

	private static long triangle(long n) {
		return n * (n + 1) / 2;
	}

	private static long pentagonal(long n) {
		return n * (3*n - 1) / 2;
	}

	private static long hexagonal(long n) {
		return n * (2*n - 1);
	}
	
/*
Inspired by: http://projecteuler.net/thread=42
Actually, I didn't understand until I did it myself...

y=x(x+1)/2 
y*2=x(x+1)
2y = x² + x
x²+x-2y = 0
d = b² - 4ac
d = 1 - 4*1*(-2)*y
d = 1 + 8y
*/
	private static boolean isTriangle(long n) {
		long d = 1 + 8*n;
		if (d < 0) return false; // sanity check!
		double x1 = (Math.sqrt(d) - 1) / 2;
		return (x1 >= 0.0 && x1 == Math.floor(x1));
	}
	
/*
y=n(3n-1)/2
2y=x(3x-1)
2y=3x²-x
0=3x²-x-2y
d=b²-4ac
d=(-1)²-4*3*(-2)*y
d=1+24y
*/
	private static boolean isPentagonal(long n) {
		long d = 1 + 24*n;
		if (d < 0) return false; // sanity check!
		double x1 = (1 + Math.sqrt(d)) / 6;
		return (x1 >= 0.0 && x1 == Math.floor(x1));
	}
	
/*
y=x(2x-1)
y=2x²-x
2x²-x-y=0
d=b²-4ac
d=(-1)²-4*2*(-y)
d=1+8y
*/
	private static boolean isHexagonal(long n) {
		long d = 1 + 8*n;
		if (d < 0) return false; // sanity check!
		double x1 = (1 + Math.sqrt(d)) / 4;
		return (x1 >= 0.0 && x1 == Math.floor(x1));
	}
	
	public static void main(String[] args) {
		//System.out.println(isTriangle(40755));
		long i = 285+1; // 285 is 40755... find the next one!
		while (true) {
			long t = triangle(i);
			if (isPentagonal(t) && isHexagonal(t)) {
				System.out.println(i + " " + t);
				break;
			}
			i++;
		}
		/*
		for (int i = 1; i <= 10; i++) {
			System.out.format("T%d = %d , P%d = %d, H%d = %d\n", i, triangle(i), i, pentagonal(i), i, hexagonal(i));
			System.out.println(isTriangle(triangle(i)) + " " + isPentagonal(pentagonal(i)) + " " + isHexagonal(hexagonal(i)));
		}
		*/
	}

}