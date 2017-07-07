// probably not a gpod idea to name the class "Exception" ... ;o

public class Exception
{
	static int[] array10 = new int[10];
	public static void main(String args[])
	{
		try
		{
			System.out.println(5 / 0);
			System.out.println(array10[11] = 999);
		}
		catch (ArithmeticException a)
		{
			System.out.println("ArithmeticException");
		}
		catch (ArrayIndexOutOfBoundsException a)
		{
			System.out.println("ArrayIndexOutOfBoundsException");
		}
	}
}
