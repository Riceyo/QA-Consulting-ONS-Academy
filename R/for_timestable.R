table <- as.integer(readline("table? "))
range <- as.integer(readline("range? "))
for (loop in 1:range)
  {
    message(table, " * ", loop, " = ", table * loop)
  }