import java.math.*;
import java.util.*;

class Euler29 {
	public static void main(String[] args) {
		HashMap<String,String> terms = new HashMap<String,String>();
		int low = 2;
		int high = 100;
		for (int a = low; a < high+1; a++) {
			for (int b = low; b < high+1; b++) {
				String key = BigInteger.valueOf(a).pow(b).toString();
				terms.put(key, key);
			}
		}
		System.out.println(terms.size());
	}
}