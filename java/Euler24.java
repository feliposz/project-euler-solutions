class Euler24 {

	static final int MAX = 10;

	public static void main(String[] args) {

		int maxCount = 1;
		int values[] = new int[MAX];
		for (int i = 0; i < MAX; i++) {
			values[i] = 0;
			maxCount *= (i+1);
		}

		int count = 0;
		
		while (count < 1000000) {
			// go to next combination (not checking permutations here)
			for (int i = MAX-1; i >= 0; i--) {
				if (i == MAX-1)
					values[i]++;
				if (values[i] >= MAX) {
					values[i] = 0;
					values[i-1]++;
				}
			}
			
			// check for repeated digits (not permutations)
			boolean repeated = false;
			for (int i = 0; i < MAX; i++) {
				for (int j = i+1; j < MAX; j++) {
					if (values[i] == values[j]) {
						repeated = true;
						break;
					}
				}
			}

			// is a permutation? count it...
			if (!repeated) {
				count++;
				/*for (int i = 0; i < MAX; i++) {
					System.out.print(values[i]);
				}
				System.out.println("");*/
			}
		}
		
		System.out.print("Last: ");
		for (int i = 0; i < MAX; i++) {
			System.out.print(values[i]);
		}
		System.out.println(" (count: " + count + ")");
	}

}