class Euler9 {

	private static boolean isPythagoreanTriplet(int a, int b, int c) {
		return (a*a + b*b) == (c*c);
	}

	public static void main(String[] args) {
		int a, b, c;
		
		for (a = 1; a <= 1000; a++) {
			for (b = a+1; a+b <= 1000; b++) {
				for (c = b+1; a+b+c <= 1000; c++) {
					//System.out.println("a = " + a + " b = " + b + " c = " + c);
					if (((a+b+c) == 1000) && isPythagoreanTriplet(a, b, c)) {
						System.out.println("a = " + a + " b = " + b + " c = " + c);
						System.out.println(a * b * c);
						return;
					}
				}
			}
		}				
	}
}
