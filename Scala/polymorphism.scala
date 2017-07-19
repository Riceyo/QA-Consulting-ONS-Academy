class draw
	{
	def drawing()
		{
		println("drawing")
		}
	}

class line extends draw
	{
	override def drawing()
		{
		println("draw line")
		}
	}
	
var x:draw = new line()
x.drawing
