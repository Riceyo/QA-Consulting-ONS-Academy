
public class SingletonBankCall
{
	public static void main(String args[])
	{
		SingletonBank hsbc, barclays, natwest;
		hsbc = SingletonBank.xyz();
		barclays = SingletonBank.xyz();
		natwest = SingletonBank.xyz();
		hsbc.a = 5;
		System.out.println(hsbc.a);
		System.out.println(barclays.a);
		System.out.println(natwest.a);
	}
}
