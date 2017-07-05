csv = read.csv("c:\\test.csv") # read csv

print(csv)

df <- data.frame(csv)

print(df)

blah <- read.csv("c:\\blah.csv",row.names=c("row1","row2","row3"),col.names=c("col1","col2","col3")) # read csv and name rows and cols 

print(blah)