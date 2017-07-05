
public class IfNested
{	
	public static void main(String args[])
	{		
		int Num;
		Num = 4500;		
		if (Num > 4000)
		{
			System.out.println("A");
			Num = Num + 100;
			if (Num > 5000)
			{
				System.out.println("B");
				System.out.println("C");
			}				
		}		
	}	
}