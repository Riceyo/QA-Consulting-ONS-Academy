import java.util.Arrays;

public class ArrayMap
{
	public static void main(String args[])
	{
		int[][] arraymap = new int[10][10];
		arraymap[0][0] = 10;
		arraymap[0][1] = 10;
		arraymap[0][2] = 10;
		arraymap[1][0] = 20;
		arraymap[1][1] = 20;
		arraymap[1][2] = 20;
		arraymap[2][0] = 30;
		arraymap[2][1] = 30;
		arraymap[2][2] = 30;
		ArrayMapMeth blah = new ArrayMapMeth();
		blah.update(arraymap, 9, 9, 9999);
		System.out.println(Arrays.deepToString(arraymap));
		blah.update(arraymap, 9, 9, 8888);
		System.out.println(Arrays.deepToString(arraymap));
		blah.remove(arraymap, 9, 9);
		System.out.println(Arrays.deepToString(arraymap));
	}
}
