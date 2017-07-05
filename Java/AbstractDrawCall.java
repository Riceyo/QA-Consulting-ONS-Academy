
public class AbstractDrawCall
{
	public static void main(String args[])
	{
		AbstractDrawExtendsCircle circle = new AbstractDrawExtendsCircle();
		AbstractDrawCallDraw drawcircle = new AbstractDrawCallDraw();
		drawcircle.calldraw(circle);
		AbstractDrawExtendsSquare square = new AbstractDrawExtendsSquare();
		AbstractDrawCallDraw drawsquare = new AbstractDrawCallDraw();
		drawsquare.calldraw(square);
		AbstractDrawExtendsLine line = new AbstractDrawExtendsLine();
		AbstractDrawCallDraw drawline = new AbstractDrawCallDraw();
		drawline.calldraw(line);
	}
}
