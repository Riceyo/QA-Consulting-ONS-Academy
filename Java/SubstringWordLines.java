
public class SubstringWordLines
{
	public static void main(String args[])
	{
		String word = "WORD1 WORD2 WORD3 WORD4 WORD5";
		for (int loop = 0; loop < word.length(); loop++)
		{
			if (word.substring(loop, loop + 1).equals(" "))
			{
				System.out.println();
			}				
			System.out.print(word.substring(loop, loop + 1).replace(" ", ""));
		}
	}
}
