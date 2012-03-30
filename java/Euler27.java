/*
http://projecteuler.net/problem=27

Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n²  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
*/

class Euler27 {

	public static boolean isPrime(long n) {
		if (n <= 1)
			return false;
		else if (n < 4)
			return true;
		else if (n % 2 == 0)
			return false;
		else if (n < 9)
			return true;
		else if (n % 3 == 0)
			return false;
		else {
			long r = (long)Math.floor(Math.sqrt(n));  /* r * r <= n*/
			long f = 5;
			while (f <= r) {
				if (n % f == 0)
					return false;
				else if (n % (f + 2) == 0)
					return false;
				f += 6;
			}
			return true;
		}
	}
	
	private static int consecutivePrimes(int a, int b) {
		int n = 0;
		while (isPrime(quadraticFormula(n, a, b))) {
			n++;
		}
		return n;
	}

	private static int printConsecutivePrimes(int a, int b) {
		int n = 0;
		while (true) {
			int p = quadraticFormula(n, a, b);
			n++;
			if (isPrime(p))
				System.out.print(p + " ");
			else
				break;
		}
		return n;
	}
	
	private static int quadraticFormula(int n, int a, int b) {
		return n*n + a*n + b;
	}

	private static final int RANGE = 1000;
	
	public static void main(String[] args) {
		int max = 0;
		int product = 0;
		//printConsecutivePrimes(-999, 61);
		
		for (int a = -RANGE; a <= RANGE; a++) {
			for (int b = -RANGE; b <= RANGE; b++) {
				int count = consecutivePrimes(a, b);
				if (count > max) {
					System.out.println("count = " + count + " a = " + a + " b = " + b);
					max = count;
					product = a * b;
				}
			}
		}
		System.out.println(product);
		
	}
}