
public class CashRegisterImproved
{
	public static void main(String args[])
	{
		int returned = 0;
		int return50 = 0;
		int return20 = 0;
		int return10 = 0;
		int return5 = 0;
		int return2 = 0;
		int return1 = 0;
		int note = 50;
		int cost = 4;
		return50 = (int) ((note - cost) / 50);
		returned = return50 * 50;
		return20 = (int) ((note - cost - returned) / 20);
		returned = returned + (return20 * 20);
		return10 = (int) ((note - cost - returned) / 10);
		returned = returned + (return10 * 10);
		return5 = (int) ((note - cost - returned) / 5);
		returned = returned + (return5 * 5);
		return2 = (int) ((note - cost - returned) / 2);
		returned = returned + (return2 * 2);
		return1 = (int) ((note - cost - returned) / 1);
		returned = returned + (return1 * 1);
		System.out.println("Note £" + note);
		System.out.println("Cost £" + cost);
		System.out.println("£50 " + return50);
		System.out.println("£20 " + return20);
		System.out.println("£10 " + return10);	
		System.out.println("£5 " + return5);
		System.out.println("£2 " + return2);
		System.out.println("£1 " + return1);
	}
}
