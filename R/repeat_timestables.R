table1 <- as.integer(readline("table1? "))
table2 <- as.integer(readline("table2? "))
if (table1 < table2)
  {
    small = table1
    big = table2
  }
if (table1 > table2)
  {
    small = table2
    big = table1
  }
loop1 = small
repeat
  {
    loop2 = 1
    repeat
      {
        print(paste(loop1, " * ", loop2, " = ", loop1 * loop2))
        if (loop2 == 12)
        {
          break
        }
        loop2 = loop2 + 1
      }
    if (loop1 == big)
      {
        break
      }
    loop1 = loop1 + 1
  }