class Euler21 {
	
	private static int sumOfDivisors(int num) {
		int result = 1;
		for (int div = 2; div <= num/2; div++) {
			if (num % div == 0) {
				result += div;
			}
		}
		return result;
	}
	
	
	public static void main(String[] args) {

		// pre-calculate all possibilities
		int d[] = new int[10000];
		for (int n = 2; n < d.length; n++) {
			d[n] = sumOfDivisors(n);
		}

		int total = 0;
		
		for (int n = 2; n < d.length; n++) {
			int a = n;
			int b = d[n];
			if (a != b && a < 10000 && b < 10000) {
				if (a == d[b] && d[a] == b) {
					System.out.println(n + " == " + d[n]);
					total += a;
				}
			}
		}
		
		System.out.println("Sum of amicable numbers = " + total);
	}
	
}
