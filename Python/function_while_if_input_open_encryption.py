def encrypt(x):
    blah = ""
    for char in x:
        blah = blah + chr(ord(char) - 1) # convert to ascii(ord), minus one, convert back to char(chr)
    print(blah)
    return blah


def decrypt(x):
    blah = ""
    for char in x:
        blah = blah + chr(ord(char) + 1) # reverse encryption
    print(blah)
    return blah


loop = 1
while loop == 1:
    print("1-encrypt\n2-decrypt\n3-quit")
    selection = input("please select an option ")
    if int(selection) == 1:
        inputfile = input("encrypt input filename? ")
        outputfile = input("encrypt output filename? ")
        inputfileobj = open(inputfile, "r")
        data = inputfileobj.read()
        print(data)
        outputfileobj = open(outputfile, "a")
        outputfileobj.write(encrypt(data))
        inputfileobj.close()
        outputfileobj.close()
    if int(selection) == 2:
        inputfile = input("decrypt input filename? ")
        outputfile = input("decrypt output filename? ")
        inputfileobj = open(inputfile, "r")
        data = inputfileobj.read()
        outputfileobj = open(outputfile, "a")
        outputfileobj.write(decrypt(data))
        inputfileobj.close()
        outputfileobj.close()
    if int(selection) == 3:
        quit()