table <- as.integer(readline("table? "))
range <- as.integer(readline("range? "))
loop <- 1
repeat
  {
    print(paste(table, " * ", loop, " = ", table * loop))
    if (loop == range)
      {
        break
      }
    loop = loop + 1
  }