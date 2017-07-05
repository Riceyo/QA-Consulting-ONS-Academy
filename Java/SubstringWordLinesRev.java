
public class SubstringWordLinesRev
{
	public static void main(String args[])
	{
		String words = "WORD1 WORD2 WORD3 WORD4 WORD5";
		int index = words.length(); // set an index to the string length
		for (int loop = words.length() - 1; loop > 0; loop--) // loop for length of the string
		{
			if (words.substring(loop, loop + 1).equals(" ")) // if find space in string
			{
				System.out.println(words.substring(loop + 1, index)); // print from current loop to current index
				index = loop; // set index to the current loop
			}
		}
		System.out.println(words.substring(0, index)); // print last word, start of string to last index
	}
}
