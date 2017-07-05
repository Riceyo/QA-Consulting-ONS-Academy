
public class HouseCall
{
	public static void main(String arg[])
	{
		House greenHouse;
		greenHouse = new House("green", 4);
		greenHouse.message();
		House redHouse = new House("red", 3);
		redHouse.message();
	}
}