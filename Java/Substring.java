
public class Substring
{
	public static void main(String args[])
	{
		String word = "RICE";
		for (int loop = 0; loop < word.length(); loop++)
		{
			//System.out.println(word);
			//System.out.println(loop);
			System.out.println(word.substring(loop, loop + 1));
		}
	}
}
