var phy = 60
var che = 70
var mat = 80
var per = (phy + che + mat) * 100 / 300

println(per + "%")

if (per < 60)
	println("fail") else
	println("pass")
