class Euler28 {
	public static void main(String[] args) {
		long sum = 1; // center
		
		for (int side = 3; side <= 1001; side += 2) {
			int topRight = side * side;
			int topLeft = topRight - side + 1;
			int bottomLeft = topLeft - side + 1;
			int bottomRight = bottomLeft - side + 1;
			System.out.print("Side = "  + side);
			System.out.println("; Corners = " + topRight + ", " + topLeft + ", " + bottomLeft + ", " + bottomRight);
			sum += topRight + topLeft + bottomLeft + bottomRight;
		}
		System.out.println("Sum = " + sum);
	}
}
