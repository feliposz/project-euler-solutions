class Euler19b {

	static int monthDays[] = {
		31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
	};

	private static boolean isLeapYear(int year) {
		return ((year % 4 == 0) && (year % 100 != 0))
			|| (year % 400 == 0);
	}

	public static void main(String[] args) {
		int count = 0;
		
		// 01/jan/1900 is monday = 1, so
		// 31/dec/1899 is sunday = 0
		int baseDay = 1;

		// advance to 1/jan/1901
		baseDay += isLeapYear(1900) ? 366 : 365;
		
		for (int year = 1901; year <= 2000; year++) {
			for (int month = 0; month < 12; month++) {
				if (baseDay % 7 == 0) {
					count++;
				}
				baseDay += monthDays[month];
				if (isLeapYear(year) && month == 1) {
					baseDay++;
				}
			}
		}
		
		System.out.println(count);
	}
}
