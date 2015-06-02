import java.io.*;
import java.util.*;

public class Euler67 {

	private static int pyramid[][];
	
	private static void loadPyramid() {
		try {
			Scanner sc = new Scanner(new File("triangle.txt"));
			pyramid = new int[100][];
			for (int i = 0; i < pyramid.length; i++) {
				pyramid[i] = new int[i+1];
				for (int j = 0; j < pyramid[i].length; j++) {
					pyramid[i][j] = sc.nextInt();
				}
			}
			sc.close();
		} catch (IOException ex) {
			System.out.println("Error: " + ex.getMessage());
		}
	}

	public static void main(String[] args) {

		loadPyramid();
	
		for (int i = pyramid.length - 1; i >= 0; i--) {
			for (int j = 0; j < pyramid[i].length; j++) {
				if (i < pyramid.length - 1) {
					int left = pyramid[i+1][j];
					int right = pyramid[i+1][j+1];
					int max = left > right ? left : right;
					pyramid[i][j] += max;
				}
			}
		}
		System.out.println(pyramid[0][0]);
	}

}
