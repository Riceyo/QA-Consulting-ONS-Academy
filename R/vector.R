vecyears <- c(1983, 1982, 2014)

print(vecyears[1])
print(vecyears[1:3])
print(vecyears[c(T,F,T)])
print(vecyears[c(T)])
print(vecyears[vecyears>2000])
print(vecyears[1] + 10) # doesn't change the values in the vector
print(max(vecyears))
print(min(vecyears))
print(mean(vecyears))
print(median(vecyears))
print(length(vecyears))
print(range(vecyears))

for (x in vecyears)
  print(x)

vecnames <- c(mam="laura", dad="richmond", baba="jaylen")

print(vecnames[1:3])
print(vecnames["baba"])