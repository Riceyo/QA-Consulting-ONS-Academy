
public class BankStaticVariableCall
	{
	public static void main(String args[])
		{	
		BankStaticVariable hsbc, natwest;
		hsbc = new BankStaticVariable();		
		hsbc.setdollar(10);
		hsbc.convertmoney(100);
		hsbc.dollarrate();
		natwest = new BankStaticVariable();
		//natwest.setdollar(10); // hsbc sets dollar
		natwest.convertmoney(20);
		natwest.dollarrate();
		}
	}
