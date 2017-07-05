
public class MathSystemCall
{
public static void main(String args[])
{
	MathSystemCallSystem meth1 = new MathSystemCallSystem();
	MathSystemExtendsMeth1 callmeth1 = new MathSystemExtendsMeth1();
	callmeth1.add(5, 5);
	MathSystemCallSystem meth2 = new MathSystemCallSystem();
	MathSystemExtendsMeth2 callmeth2 = new MathSystemExtendsMeth2();
	callmeth2.add(5, 5);
	MathSystemCallSystem meth3 = new MathSystemCallSystem();
	MathSystemExtendsMeth3 callmeth3 = new MathSystemExtendsMeth3();
	callmeth3.add(5, 5);	
}
}
