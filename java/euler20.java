import java.math.*;

class Euler20 {

	private static BigInteger bigFactorial(int num) {
		BigInteger result = BigInteger.ONE;
		for (int i = 1; i <= num; i++) {
			result = result.multiply(BigInteger.valueOf(i));
		}		
		return result;
	}

	public static void main(String[] args) {
		String str = bigFactorial(100).toString();
		int total = 0;
		for (int i = 0; i < str.length(); i++) {
			char c = str.charAt(i);
			total += (c - '0');
		}
		System.out.println(total);
	}
}