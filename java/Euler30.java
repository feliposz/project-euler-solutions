class Euler30 {

	private static int sumDigits(int num, int exp) {
		int sum = 0;
		while (num > 0) {
			sum += (int)Math.pow(num % 10, exp);
			num /= 10;
		}
		return sum;
	}

	public static void main(String[] args) {
		long sum = 0;		
		long maxLimit = 9 * (int)Math.pow(9, 5);
		
		for (int num = 10; num <= maxLimit; num++) {
			if (num == sumDigits(num, 5)) {
				System.out.println(num);
				sum += num;
			}
		}
		System.out.println("Sum = " + sum);
	}
}
