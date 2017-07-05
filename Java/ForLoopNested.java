
public class ForLoopNested
{
	public static void main(String args[])
	{
		int a = 1;
		int b = 1;
		for (; a <= 5; a++)
		{
			b = 1;
			for (; b <= 5; b++)
			{
				System.out.println(a + " " + b);
			}
		}
	}
}