
public class SwitchDayNames
{
	public static void main(String args[])
	{
		int daynumber = 3;
		String dayname = null;
		switch (daynumber)
		{
		case 1: dayname = "Mon";
		break;
		case 2: dayname = "Tue";
		break;
		case 3: dayname = "Wed";
		break;
		default: dayname = "Invalid";
		break;
		}
		System.out.println(daynumber + " - " + dayname);
	}
}
