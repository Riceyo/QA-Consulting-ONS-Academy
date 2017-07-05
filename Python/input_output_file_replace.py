inputfile = input("filename? ")
replacewhat = input("replace what? ")
replacewith = input("replace with? ")
outputfile = input("new filename? ")
inputfileobj = open(inputfile, "r")
data = inputfileobj.read()
outputfileobj = open(outputfile, "w")
outputfileobj.write(data.replace(replacewhat, replacewith))
inputfileobj.close
outputfileobj.close