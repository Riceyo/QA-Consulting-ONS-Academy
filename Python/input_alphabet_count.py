inputstring = input("input alphabet string ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for loop in alphabet:
    if inputstring.count(loop) > 0:
        print(loop, end="")
        print("-", end="")
        print(inputstring.count(loop), end="")
        print("")