num1 = input("Enter number ")
x = int(num1)
if x > 100:
	print("> 100")
	if x > 500:
		print("> 500")
	else:
		print("< 500")
else:
	print("< 100")
	if x < 50:
		print("< 50")
	else:
		print("> 50")