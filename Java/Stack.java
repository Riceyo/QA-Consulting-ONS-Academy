import java.util.Arrays;

public class Stack
{
	public static void main(String[] args)
	{
		int[] array = new int[10];
		StackMeth stack = new StackMeth();
		System.out.println(Arrays.toString(array));
		stack.stackpush(array, 10);
		stack.stackpush(array, 20);
		stack.stackpush(array, 30);
		System.out.println(Arrays.toString(array));
	}
}
