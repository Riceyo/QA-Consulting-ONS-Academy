
public class DivideModulusMany
	{
	public static void main(String args[])
		{
		int num, nummodulus1, nummodulus2, nummodulus3, nummodulus4, nummodulus5;
		num = 12345;
		nummodulus1 = num % 10;
		nummodulus2 = num / 10 % 10;
		nummodulus3 = num / 100 % 10;
		nummodulus4 = num / 1000 % 10;
		nummodulus5 = num / 10000 % 10;
		System.out.println(nummodulus1);
		System.out.println(nummodulus2);
		System.out.println(nummodulus3);
		System.out.println(nummodulus4);
		System.out.println(nummodulus5);
		}
	}
