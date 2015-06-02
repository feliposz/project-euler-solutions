import java.util.*;

class Euler19 {
	public static void main(String[] args) {
		Calendar cal = Calendar.getInstance();
		int count = 0;
		for (int year = 1901; year <= 2000; year++) {
			for (int month = 0; month < 12; month++) {
				cal.set(year, month, 1);
				if (cal.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY)
					count++;
			}
		}
		System.out.println(count);
	}
}
