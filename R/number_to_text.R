#inputnum <- readline("1-9999 number? ")
inputnum <- "222"

num2text <- function(x)
  {
    return(
      switch(
        x,
        "1" = "one",
        "2" = "two",
        "3" = "three",
        "4" = "four",
        "5" = "five",
        "6" = "six",
        "7" = "seven",
        "8" = "eight",
        "9" = "nine",
        "10" = "ten",
        "11" = "eleven",
        "12" = "twelve",
        "13" = "thirteen",
        "14" = "fourteen",
        "15" = "fifteen",
        "16" = "sixteen",
        "17" = "seventeen",
        "18" = "eighteen",
        "19" = "nineteen",
        "20" = "twenty",
        "30" = "thirty",
        "40" = "forty",
        "50" = "fifty",
        "60" = "sixty",
        "70" = "seventy",
        "80" = "eighty",
        "90" = "ninety"
      )
    )
  }

if (length(str(inputnum)) == 1) {inputnum = 000 & inputnum}
if (length(str(inputnum)) == 2) {inputnum = 00 & inputnum}
if (length(str(inputnum)) == 3) {inputnum = 0 & inputnum}

num1 <- as.integer(inputnum) %% 10
num2 <- (as.integer(inputnum) / 10) %% 10
num3 <- (as.integer(inputnum) / 100) %% 10
num4 <- (as.integer(inputnum) / 1000) %% 10

num1 <- as.integer(num1)
num2 <- as.integer(num2)
num3 <- as.integer(num3)
num4 <- as.integer(num4)

print(num1)
print(num2)
print(num3)
print(num4)

if (inputnum < 21) {print(num2text(inputnum))}
if (inputnum > 20 & num4 == 0 & num3 == 0 & num2 == 0 & num1 == 0) {print(num2text(inputnum))}
if (inputnum > 20 & num4 == 0 & num3 == 0 & num2 > 0 & num1 > 0) {paste(num2text(toString(num2 * 10)), num2text(toString(num1)))}
if (inputnum > 20 & num4 == 0 & num3 > 0 & num2 == 0 & num1 == 0) {paste(num2text(toString(num3)), "hundred")}
if (inputnum > 20 & num4 == 0 & num3 > 0 & num2 > 0 & num1 == 0) {paste(num2text(toString(num3)), "hundred and", num2text(toString(num2 * 10)))}
if (inputnum > 20 & num4 == 0 & num3 > 0 & num2 > 0 & num1 > 0) {paste(num2text(toString(num3)), "hundred and", num2text(toString(num2 * 10)), num2text(toString(num1)))}
# thousands code here...