
public class ForLoopNestedOddEven
{
	public static void main(String args[])
	{
		int mynumber = 10;
		int loop;
		int oddloop;	
		for (loop = 1; loop <= mynumber; loop++) // loop number of times as the variable value passed
		{
			if (loop % 2 > 0) // if looping on an odd number
			{
				for (oddloop = 1; oddloop <= loop; oddloop++) // loop number of times as the odd number				
				{						
					System.out.print(oddloop); // display the odd number loop
				}
				System.out.println(); // start new line
			}
			else
			{
				System.out.println(loop); // display the current loop
			}
		}
	}
}
