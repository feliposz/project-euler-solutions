public class NumberToWords {

	private static String[] regular = {"zero", "one", "two", "three", "four",
		"five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
		"thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
		"nineteen",
	};
	
	private static String[] tens = {null, null, "twenty", "thirty", "forty",
		"fifty", "sixty", "seventy", "eighty", "ninety",
	};

	private static String convert(int num) {
		if (num < 20) {
			return regular[num];
		} else if (num < 100) {
			int tensIndex = num / 10;
			int onesIndex = num % 10;
			if (onesIndex > 0)
				return tens[tensIndex] + "-" + regular[onesIndex];
			else
				return tens[tensIndex];
		} else if (num < 1000) {
			int hundreds = num / 100;
			int others = num % 100;
			if (others > 0)
				return convert(hundreds) + " hundred and " + convert(others);
			else
				return convert(hundreds) + " hundred";
		} else if (num < 1000000) {
			int thousands = num / 1000;
			int others = num % 1000;
			String strThousands = "thousands";
			if (thousands == 1)
				strThousands = "thousand";
			if (others > 0)
				return convert(thousands) + " " + strThousands + " " +
					   convert(others);
			else
				return convert(thousands) + " " + strThousands;
		} else {
			return "";
		}
	}
		
	public static void main(String[] args) {
		String str = "";
		for (int i = 1; i <= 1000; i++) {
			str += convert(i);
			System.out.println(i + " " + convert(i));
		}
		str = str.replaceAll(" ", "").replaceAll("-", "");
		System.out.println("Letters used = " + str.length());
	}
	
}