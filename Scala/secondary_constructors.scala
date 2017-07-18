class secondaryconstructors
	{
	def this(a:Int, b:Int) // this secondary constructor is called when two parameters are passed to the primary constructor
		{
		this() // must be first
		var add = a + b
		println(add)
		}
	def this(a:Int, b:Int, c:Int) // this secondary constructor is called when three parameters are passed to the primary constructor
		{
		this() // must be first
		var add = a + b + c
		println(add)
		}
	}
	
var twoparameters = new secondaryconstructors(1, 2)

var threeparameters = new secondaryconstructors(1, 2, 3)
