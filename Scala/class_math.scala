class math(x:Int, y:Int)
	{
	var a:Int = x
	var b:Int = y
	def add()
		{
		println(a+b)
		}
	def sub()
		{
		println(a-b)
		}
	def mul()
		{
		println(a*b)
		}
	def div()
		{
		println(a/b)
		}
	println("test - primary constructor")
	}

var m = new math(2,5)
m.add
m.sub
m.mul
m.div
