num1 = int(input("Enter Number "))
num2 = int(input("Enter Number "))
if num1 < num2:
    small = num1
    big = num2
else:
    small = num2
    big = num1
for loop1 in range(big, small - 1, -1):
    for loop2 in range(1, 13):
        print("%d x %d = %d" % (loop1, loop2, loop1*loop2))
