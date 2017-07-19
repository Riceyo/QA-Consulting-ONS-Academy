class draw
	{
	def drawing()
		{
		println("draw - drawing")
		}
	}

class line extends draw
	{
	override def drawing() // this method must be overwritten to be used
		{
		println("line - drawing")
		}
	def writing()
		{
		println("line - writing") // this method cannot be used as it's not inherited
		}
	}
	
var x:draw = new line() // create reference variable of parent class and store address of child class
x.drawing // call overwritten inherited method
