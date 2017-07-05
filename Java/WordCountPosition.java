public class WordCountPosition {
	public static void main (String x[])
	{
		String sentence = "the quick brown fox jumps over the lazy dog";
		String findword = "the";
		int foundwordcount = 0;
		String findwordposition =  "";
		String findwordloop = "";
		for(int loop = 0; loop < sentence.length(); loop++) // loop through the length of the sentence
		{			
			if(loop + findword.length() <= sentence.length()) // if the current loop plus word to find doesn't exceed the sentence length
			{
				findwordloop = sentence.substring(loop, loop + findword.length()); // chop the sentence up into lengths of the word to find
				System.out.println(findwordloop);
				if(findwordloop.equals(findword)) // if the current chopped up segment matches the word to find
				{
					foundwordcount++; // add to the found words count variable
					findwordposition = findwordposition + loop + " "; // add the current position to a string variable
				}
			}
		}
		System.out.println("Count: " + foundwordcount);
		System.out.println("Position: " + findwordposition);
	}
}