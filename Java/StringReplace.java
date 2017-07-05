public class StringReplace
{
	public static void main (String args[])
	{
		String sentence = "the quick brown fox jumped over the lazy dog";
		sentence = sentence.replaceAll("the", "THE");
		System.out.print(sentence);	
	}
}