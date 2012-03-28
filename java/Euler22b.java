import java.io.*;
import java.util.*;

class Euler22b {

	private static int calcValue(String name) {
		int total = 0;
		for (int i = 0; i < name.length(); i++) {
			total += name.charAt(i) - 'A' + 1;
		}
		return total;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader rd = new BufferedReader(new FileReader("names.txt"));
		String[] nameArray = rd.readLine().replace("\"", "").split(",");
		Arrays.sort(nameArray);
		int total = 0;
		for (int i = 0; i < nameArray.length; i++) {
			int pos = i + 1;
			int value = calcValue(nameArray[i]);
			total += pos * value;
		}
		System.out.println(total);
	}
	
}
