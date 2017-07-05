loop = 1
try:
    while loop == 1:
        print("1-addition\n2-subtraction\n3-multiplication\n4-division\n5-timestable\n6-quit")
        selection = input("please select an option ")
        def numberinputa():
            return input("please enter a number ")
        def numberinputb():
            return input("please enter a number ")
        def addition(a, b):
            return a + b
        def subtraction(a, b):
            return a - b
        def multiplication(a, b):
            return a * b
        def division(a, b):
            return a / b
        def timestable(a, b):
            for timestableloopprint in range(1, b + 1):
                print("%d x %d = %d" % (a, timestableloopprint, a * timestableloopprint))
        if int(selection) == 1:
            additionloop = 1
            while additionloop == 1:
                print(addition(int(numberinputa()), int(numberinputb())))
                if input("repeat? ") == "n":
                    additionloop = 0
        if int(selection) == 2:
            subtractionloop = 1
            while subtractionloop == 1:
                print(subtraction(int(numberinputa()), int(numberinputb())))
                if input("repeat? ") == "n":
                    subtractionloop = 0
        if int(selection) == 3:
            multiplicationloop = 1
            while multiplicationloop == 1:
                print(multiplication(int(numberinputa()), int(numberinputb())))
                if input("repeat? ") == "n":
                    multiplicationloop = 0
        if int(selection) == 4:
            divisionloop = 1
            while divisionloop == 1:
                print(division(int(numberinputa()), int(numberinputb())))
                if input("repeat? ") == "n":
                    divisionloop = 0
        if int(selection) == 5:
            timestableloop = 1
            while timestableloop == 1:
                a = input("please enter times table ")
                b = input("please enter how many to calculate ")
                timestable(int(a), int(b))
                if input("repeat? ") == "n":
                    timestableloop = 0
        if int(selection) == 6:
            quit()
except ZeroDivisionError:
    print("cannot divide by zero")