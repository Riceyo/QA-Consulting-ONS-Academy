
public class ConstructorThis
{
	public ConstructorThis(int a) // constructor with 1 parameter
	{
		this(a, a); // calls same name constructor with 2 parameters
		System.out.println(a);
	}
	public ConstructorThis(int a, int b) // constructor with 2 parameters
	{
		this(a, a, a); // calls same name constructor with 3 parameters
		System.out.println(a + "" + b);
	}
	public ConstructorThis(int a, int b, int c) // constructor with 3 parameters
	{
		System.out.println(a + "" + b + "" + c);
	}
}
