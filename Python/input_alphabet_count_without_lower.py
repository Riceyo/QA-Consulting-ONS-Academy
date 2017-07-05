# inputstring = input("input alphabet string ")

inputstring = "aaAAbbBBccCC"

alphabetsmall = "abcdefghijklmnopqrstuvwxyz"
alphabetbig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for loopsmall in alphabetsmall:
    countsmall = inputstring.count(loopsmall)
    alphabetsmall = alphabetsmall[1:]
    for loopbig in alphabetbig[:1]:
        countbig = inputstring.count(loopbig)
        alphabetbig = alphabetbig[1:]
        if countsmall + countbig > 0:
            print(loopsmall, end="")
            print(countsmall + countbig, end="")
            print("")
