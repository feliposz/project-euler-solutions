class Euler48 {

	private static long power(int b, int e) {
		long res = 1;
		for (int i=0; i<e && res != 0; i++) {
			// consider only last ten digits
			// also, avoids overflow
			res = (res * b) % 10000000000L;
		}
		return res;
	}
	
	public static void main(String[] args) {
		long res = 0;
		for (int i=1; i<=1000; i++) {
			res += power(i, i);
		}
		System.out.println(res % 10000000000L);
	}
}