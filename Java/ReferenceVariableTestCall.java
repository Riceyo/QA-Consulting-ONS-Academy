
public class ReferenceVariableTestCall
{
	public static void main(String args[])
	{
		ReferenceVariableTest blah = new ReferenceVariableExtendsTest();
		blah = new ReferenceVariableExtendsTest();
		blah.message1();
		blah.message2();
		blah.message3();
	}
}
