
public class CashRegister
{
	public static void main(String args[])
	{
		int note, cost, return50, return20, return10, return5;
		return50 = 0;
		return20 = 0;
		return10 = 0;
		return5 = 0;
		note = 50;
		cost = 15;
		return50 = (note - cost) / 50;
		return20 = (note - cost - (50 * return50)) / 20;
		return10 = (note - cost - - (50 * return50) - (20 * return20)) / 10;			
		return5 = (note - cost - (50 * return50) - (20 * return20) - (10 * return10)) / 5;		
		System.out.println(return50);
		System.out.println(return20);
		System.out.println(return10);
		System.out.println(return5);
	}
}
