table1 <- as.integer(readline("table1? "))
table2 <- as.integer(readline("table2? "))
if (table1 < table2)
  {
    small = table1
    big = table2
  }
if (table2 < table1)
  {
    small = table2
    big = table1
  }
for (loop1 in seq(small, big))
  {
    for (loop2 in seq(1,12))
      {
        print(paste(loop1, " * ", loop2, " = ", loop1 * loop2))
      }
  }