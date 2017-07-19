class results
	{
	private var varphy : Int = 0
	def phy_= (a : Int) // property setter method
		{
		if ((a > 0) & (a < 101)) 
			{
			varphy = a // if valid result keep as is
			}
		else
			{
			varphy = 0 // if invalid result set to zero
			}
		}
	def phy : Int = // property getter method
		{
		return varphy
		}
	}
	
var richmond = new results()
richmond.phy = 70
var richmondres = richmond.phy
println("richmond: " + richmondres)

var luke = new results()
luke.phy = 101
var lukeres = luke.phy
println("luke: " + lukeres)

var david = new results()
david.phy = 99
var davidres = david.phy
print("david: " + davidres)
