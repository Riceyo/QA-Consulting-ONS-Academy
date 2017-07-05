
public class Split 
{
	public static void main(String args[])
	{
		String textmatch = "the";
		String sentence = "the quick brown fox jumped over the lazy dog";
		String[] sentencesplit = sentence.split(" ");
		int matchcount = 0;
		for(String word: sentencesplit)
		{
			if(word.equals(textmatch))
				//matchcount = matchcount + 1;
				matchcount++; // alternative
		}
		System.out.println(matchcount);
	}
}