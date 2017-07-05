day1 <- switch(1, "mon", "tue", "wed", "thu", "fri", "sat", "sun")
day2 <- switch(2, "mon", "tue", "wed", "thu", "fri", "sat", "sun")

print(day1)
print(day2)

askday <- as.integer(readline("day number? "))

print(switch(askday, "mon", "tue", "wed", "thu", "fri", "sat", "sun"))

askabc <- readline("abc? ")

print(switch(askabc, "a" = "alpha", "b" = "bravo", "c" = "charlie"))