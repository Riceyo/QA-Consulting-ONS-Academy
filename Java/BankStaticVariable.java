
public class BankStaticVariable 
{
	static int dollar;
	int x;
	public void setdollar(int a)
	{
		dollar = a;
	}
	public void convertmoney(int x)
	{
		System.out.println(x * dollar);
	}
	public void dollarrate()
	{
		System.out.println("dollar: " + dollar);
	}
}
