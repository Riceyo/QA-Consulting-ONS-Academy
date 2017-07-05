sum <- function(num1, num2) {return (num1 + num2)}

print(sum(5, 5))

print(do.call(sum, list(7, 7)))

print(args(sum)) # ?

print(body(sum))

sumpass <- sum

print(sumpass(2, 2))

div <- function()
{
  nesteddiv <- function(num1, num2) {return (num1 / num2)}
}

divpass <- div()
print(paste("divpass", divpass(5, 2)))

globalvar <- "globalvar"
print(globalvar)

funct <- function()
{
  print(globalvar)
  globalvar <- "localvar" # new local variable (same name as global variable)
  print(globalvar) # print local variable
  newvar <- "newvar" # new local variable
  print(newvar)
  globalvar <<- "globalvar updated from funct" # <<- updates global variable
  print(globalvar) # print the local variable (same name as global variable)
  nestedfunct <- function()
  {
    globalvar <- "nestedlocalvar" # new local variable (same name as global variable)
    print(globalvar) # print the local variable (same name as global variable)
    globalvar <<- "globalvar updated from nested funct" # <<- updates variable level up only
  }
  nestedfunct()
  print(globalvar)
}

funct()

print(globalvar)