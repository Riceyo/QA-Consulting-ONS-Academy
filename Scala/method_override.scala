class one
	{
	def message()
		{
		println("class one")
		}
	}

class two extends one
	{
	override def message()
		{
		println("class two")
		}
	}
	
var classone = new one
classone.message()

var classtwo = new two
classtwo.message()
