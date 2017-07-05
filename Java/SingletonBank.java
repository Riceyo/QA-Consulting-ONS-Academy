
public class SingletonBank
{
	int a;
	static SingletonBank r;
	public void msg()
	{
		System.out.println("Hello");
	}
	private SingletonBank()
	{
		// private default constructor
	}
	public static SingletonBank xyz() // method which returns class
	{
		if (r == null)
		{
			r = new SingletonBank();
		}
		return r;
	}
}
