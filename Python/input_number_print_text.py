inputnum = int(input("1-9999 number? "))

array = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
        70: "seventy", 80: "eighty", 90: "ninety"}

if len(str(inputnum)) == 1:
    inputnum = 000 + inputnum

if len(str(inputnum)) == 2:
    inputnum = 00 + inputnum

if len(str(inputnum)) == 3:
    inputnum = 0 + inputnum

num1 = int(inputnum % 10)
num2 = int(inputnum / 10 % 10)
num3 = int(inputnum / 100 % 10)
num4 = int(inputnum / 1000 % 10)

if inputnum < 21:
    print(array[inputnum])
    quit()

if num4 == 0 and num3 == 0 and num1 == 0 and inputnum > 20:
    print(array[inputnum])
    quit()

if num4 == 0 and num3 == 0 and inputnum > 20:
    print(array[int(str(num2) + str(0))], end="")
    print(" ", end="")
    print(array[num1], end="")
    quit()

if num4 == 0 and num3 > 0 and num2 == 0 and num1 == 0:
    print(array[int(str(num3))], end="")
    print(" hundred", end="")
    quit()

if num4 == 0 and num3 > 0 and int(str(inputnum)[-2:]) < 21:
    print(array[int(str(num3))], end="")
    print(" hundred and ", end="")
    print(array[int(str(inputnum)[-2:])], end="")
    quit()

# UNFINISHED