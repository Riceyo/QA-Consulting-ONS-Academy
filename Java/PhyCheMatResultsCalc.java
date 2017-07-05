
public class PhyCheMatResultsCalc
{	
	int phy, che, mat;
	float total, per;	
	public void calc()
	{
		total = phy + che + mat;
		per = total * 100 / 300;
	}	
	public void display()
	{
		System.out.println("total: " + total);
		System.out.println("per: " + per);
	}
}
