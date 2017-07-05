
public class IfElseNested
{
	public static void main(String args[])
	{
		int input;
		input = 2001;
		if (input > 2000)
		{
			System.out.println("A");
			if (input > 5000)
				System.out.println("C");
			else
				System.out.println("D");
			System.out.println("E");
		}
		else
		{
			System.out.println("B");
			if (input > 1500)
				System.out.println("2");
		}
	}
}