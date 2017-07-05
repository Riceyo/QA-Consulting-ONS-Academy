import java.util.Arrays;

public class Array
{
	public static void main(String[] args)
	{
		int[] array = new int[10];
		array[0] = 10;
		array[1] = 5;
		array[2] = 20;
		array[3] = 15;
		array[4] = 15;
		array[5] = 999;
		array[6] = 2;
		array[7] = 1983;
		array[8] = 7;
		array[9] = 8888;	
		Arrays.sort(array);
		System.out.println("Lowest: " + array[0]);
		System.out.println("Highest: " + array[array.length - 1]);
		System.out.println("Order: " + Arrays.toString(array));
		ArrayInterfaceMeth blah = new ArrayInterfaceMeth();
		blah.highest();
		blah.lowest();
		blah.order();
	}
}
