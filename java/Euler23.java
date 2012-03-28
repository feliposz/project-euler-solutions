import java.util.*;

// took 80 seconds!!!

class Euler23 {

	private static final int MAX = 28123;

	private static int sumOfDivisors(int n) {
		int sum = 0;
		for (int i = 1; i <= n/2; i++) {
			if (n % i == 0)
				sum += i;
		}
		return sum;
	}
	
	public static void main(String[] args) {
		
		ArrayList<Integer> abundant = new ArrayList<Integer>();
	
		System.out.print("Creating list of abundants...");
		for (int i = 1; i < MAX; i++) {
			int sod = sumOfDivisors(i);
			if (sod > i)
				abundant.add(i);
		}
		System.out.println("done.");

		System.out.println("abundants = " + abundant.size());
		
		int countRepresentable = 0;
		int countNonRepresentable = 0;
		long sumOfNonRepresentable = 0;
		
		System.out.println("Searching for numbers representable by the sum of 2 abundants.");
		
		for (int num = 1; num < MAX; num++) {
			boolean representable = false;
			for (int i = 0; i < abundant.size() && num > abundant.get(i); i++) {
				int otherNum = num - abundant.get(i);
				if (abundant.contains(otherNum)) {
					representable = true;
					break;
				}
			}
			if (!representable) {
				System.out.print(".");
				countNonRepresentable++;
				sumOfNonRepresentable += num;
			}
		}
		
		System.out.println("done!");
		System.out.println("Non-Representable by 2 abundants: " + countNonRepresentable);
		System.out.println("Sum of Non-Representable: " + sumOfNonRepresentable);
	}

}