var num : String = "3891"

def num2text(num:Int):String=
	{
	num match
		{
		case 1 => "one"
        case 2 => "two"
        case 3 => "three"
        case 4 => "four"
        case 5 => "five"
        case 6 => "six"
        case 7 => "seven"
        case 8 => "eight"
        case 9 => "nine"
        case 10 => "ten"
        case 11 => "eleven"
        case 12 => "twelve"
        case 13 => "thirteen"
        case 14 => "fourteen"
        case 15 => "fifteen"
        case 16 => "sixteen"
        case 17 => "seventeen"
        case 18 => "eighteen"
        case 19 => "nineteen"
        case 20 => "twenty"
        case 30 => "thirty"
        case 40 => "forty"
        case 50 => "fifty"
        case 60 => "sixty"
        case 70 => "seventy"
        case 80 => "eighty"
        case 90 => "ninety"
		}
	}
	
if (num.length == 1) {num = "000" + num}
if (num.length == 2) {num = "00" + num}
if (num.length == 3) {num = "00" + num}

val num1 = (num.toInt % 10)
val num2 = (num.toInt / 10 % 10)
val num3 = (num.toInt / 100 % 10)
val num4 = (num.toInt / 1000 % 10)
val num2num1 = (num2.toString + num1.toString)

println("num1 - " + num1)
println("num2 - " + num2)
println("num3 - " + num3)
println("num4 - " + num4)
println("num2num1 - " + num2num1)

if (num.toInt < 21) {print(num2text(num2num1.toInt))}
if (num.toInt > 20 & num4 == 0 & num3 == 0 & num2 > 0 & num1 == 0) {print(num2text(num2 * 10))}
if (num.toInt > 20 & num4 == 0 & num3 == 0 & num2 > 0 & num1 > 0) {print(num2text(num2 * 10) + " " + num2text(num1))}
if (num.toInt > 20 & num4 == 0 & num3 > 0 & num2 == 0 & num1 == 0) {print(num2text(num3) + " hundred")}
if (num.toInt > 20 & num4 == 0 & num3 > 0 & num2 > 0 & num1 == 0) {print(num2text(num3) + " hundred and " + num2text(num2 * 10))}
if (num.toInt > 20 & num4 == 0 & num3 > 0 & num2 > 0 & num1 > 0 & num2num1.toInt < 21) {print(num2text(num3) + " hundred and " + num2text(num2num1.toInt))}
if (num.toInt > 20 & num4 == 0 & num3 > 0 & num2 > 0 & num1 > 0 & num2num1.toInt > 21) {print(num2text(num3) + " hundred and " + num2text(num2 * 10) + " " + num2text(num1))}
if (num.toInt > 20 & num4 > 0 & num3 == 0 & num2 == 0 & num1 == 0) {print(num2text(num4) + " thousand")}
if (num.toInt > 20 & num4 > 0 & num3 == 0 & num2 > 0 & num1 > 0 & num2num1.toInt < 21) {print(num2text(num4) + " thousand and " + num2text(num2num1.toInt))}
if (num.toInt > 20 & num4 > 0 & num3 == 0 & num2 == 0 & num1 > 0) {print(num2text(num4) + " thousand and " + num2text(num1))}
if (num.toInt > 20 & num4 > 0 & num3 > 0 & num2 == 0 & num1 == 0) {print(num2text(num4) + " thousand, " + num2text(num3) + " hundred")}
if (num.toInt > 20 & num4 > 0 & num3 > 0 & num2 > 0 & num1 == 0) {print(num2text(num4) + " thousand, " + num2text(num3) + " hundred and " + num2text(num2 * 10))}
if (num.toInt > 20 & num4 > 0 & num3 > 0 & num2 > 0 & num1 > 0) {print(num2text(num4) + " thousand, " + num2text(num3) + " hundred and " + num2text(num2 * 10) + " " + num2text(num1))}
