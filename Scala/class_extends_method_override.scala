class one
	{
	def message()
		{
		println("class one")
		}
	}

class two extends one // inherit
	{
	override def message() // override the method that was inherited
		{
		println("class two")
		}
	}
	
var classone = new one
classone.message()

var classtwo = new two
classtwo.message()
