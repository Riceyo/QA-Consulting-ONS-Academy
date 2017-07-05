
public class House
{
	String colour;
	int rooms;
	public House(String colour, int rooms)
	{
		this.colour = colour;
		this.rooms = rooms;
	}
	public void message()
	{
		System.out.println("My " + colour + " house has " + rooms + " rooms.");
	}
}
