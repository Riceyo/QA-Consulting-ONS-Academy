
public class BinaryConvert
{
	public static void main(String args[])
	{
		String binaryoutput = "";
		int mynumber = 0;
		for (mynumber = 5; mynumber > 0;)
		{
			if (mynumber % 2 > 0)
			{
				binaryoutput = "1" + binaryoutput;		
			}
			else
			{
				binaryoutput = "0" + binaryoutput;
			}
			mynumber = mynumber / 2;
		}
		System.out.println(binaryoutput);
	}
}
