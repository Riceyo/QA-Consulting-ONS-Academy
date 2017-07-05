
public class BinaryConvertReverse
{
	public static void main(String args[])
	{
		String binary = "01010";
		int output = 0;
		for (int loop = 0; loop < binary.length(); loop++)
		{
			System.out.println("loop - " + loop);
			output = output * 2;
			System.out.println("output * 2 - " + output);
			if (binary.charAt(loop) == '0')
			{
				output = output + 0;
			}
			else
			{
				output = output + 1;
			}
			System.out.println("output after if - " + output);
		}
		System.out.println("answer - " + output);
	}
}
