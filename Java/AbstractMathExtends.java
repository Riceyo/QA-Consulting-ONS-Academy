
public class AbstractMathExtends extends AbstractMath // inherit class
{
	public void addition(int a, int b) // overwrite method
	{
		System.out.println(a + " + " + b + " = " + (a + b)); // improvements
	}
	public void subtraction(int a, int b) // overwrite method
	{
		System.out.println(a + " - " + b + " = " + (a - b)); // improvements
	}
	public void multiplication(int a, int b) // overwrite method
	{
		System.out.println(a + " * " + b + " = " + (a * b)); // improvements
	}
	public void division(int a, int b) // overwrite method
	{
		System.out.println(a + " / " + b + " = " + (a / b)); // improvements
	}
}
