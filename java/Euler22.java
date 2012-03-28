import java.io.*;
import java.util.*;
class Euler22 {
	public static void main(String[] args) throws IOException {
		ArrayList<String> nameList = new ArrayList<String>();
		FileReader rd = new FileReader("names.txt");
		/*
		String name = "";
		while (true) {
			int c = rd.read();
			if (c == '"') {
				continue;
			} else if (c == ',') {
				nameList.add(name);
				name = "";
			} else if (c == -1) {
				nameList.add(name);
				break;
			} else {
				name += (char)c;
			}
		}*/		
		String[] nameArray = new String[nameList.size()];
		nameArray = nameList.toArray(nameArray);
		Arrays.sort(nameArray);
		for (int i = 0; i < nameArray.length; i++) {
			System.out.println(nameArray[i]);
		}
	}
}

//NOTE: NOT FINISHED, refactored to Euler22b