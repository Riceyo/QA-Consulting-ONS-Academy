
public class ArrayMapMeth
{
	public void update(int[][] arraymap, int a, int b, int z)
	{
		arraymap[a][b] = z;
	}
	public void remove(int[][] arraymap, int a, int b)
	{
		arraymap[a][b] = 0;
	}
}
