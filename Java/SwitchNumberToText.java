
public class SwitchNumberToText
{		
	public static void main(String args[])
	{
		int num, no1, no2, no3, no4;
		String blah;
		num = 1234;
		no1 = num % 10;
		no2 = num / 10 % 10;
		no3 = num / 100 % 10;
		no4 = num / 1000 % 10;
		blah = NumberText(no4);
		blah = blah + " " + NumberText(no3);
		blah = blah + " " + NumberText(no2);
		blah = blah + " " + NumberText(no1);	
		System.out.println(blah);
	}
	public static String NumberText(int num)
	{
		String Word = "";
		switch (num)
		{
		case 1: Word = "One";
		break;
		case 2: Word = "Two";
		break;
		case 3: Word = "Three";
		break;
		case 4: Word = "Four";
		break;
		case 5: Word = "Five";
		break;
		case 6: Word = "Six";
		break;
		case 7: Word = "Seven";
		break;
		case 8: Word = "Eight";
		break;
		case 9: Word = "Nine";
		break;
		case 0: Word = "Zero";
		break;
		}	
		return Word;
	}
}
