
public class PhyCheMatResultsPassedCalc
{	
	private int phy, che, mat, passed;
	private float total, per;	
	public void display()
	{
		if (phy == -1 || che == -1 || mat == -1)
			System.out.println("Invalid");
		else
		{
			total = phy + che + mat;
			per = total * 100 / 300;
			System.out.println("Total: " + total);
			System.out.println("Per: " + per);
			System.out.println("Passed: " + passed);
			if (passed == 0)
				System.out.println("Go home");
			if (passed == 1)
				System.out.println("Retake course");
			if (passed == 2)
				System.out.println("Retake exam");
		}
	}
	public void physics(int a)
	{
		che = -1;
		if (a >= 0 & a <= 100)
			che = a;
		else
			System.out.println("Physics Invalid");
		if (che >= 70)
			passed = passed + 1;
	}
	public void chemistry(int a)
	{
		phy = -1;
		if (a >= 0 & a <= 100)
			phy = a;
		else
			System.out.println("Chemistry Invalid");
		if (phy >= 70)
			passed = passed + 1;
	}
	public void mathematics(int a)
	{
		mat = -1;
		if (a >= 0 & a <= 100)
			mat = a;
		else
			System.out.println("Mathematics Invalid");
		if (mat >= 70)
			passed = passed + 1;		
	}
}
