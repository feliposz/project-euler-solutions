/* Project Euler - Problem 3 solution
 * Using the long type, since there are no 
 */

class Euler3b {
	public static void main(String[] args) {
		//long num = 13195;
		long num = 600851475143L;
		//long num =   9999999999999L;
		//long num =   179426549L;
		//long num =   179426549L;
		long f = 2;
		long last = 0;
		while (num > 1) {
			//System.out.println("DEBUG => f: " + f + " last: " + last + " num: " + num);
			if (num % f == 0) {
				System.out.println("Divisible by f: " + f + " num: " + num);
				while (num % f == 0 && num > 1) {
					num /= f;
				}
				last = f;
			}
			f++;
		}
		System.out.println("Largest factor: " + last);
	}
}
