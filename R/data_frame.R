phy <- c(93,82,69) # vector phy results
che <- c(98,78,69) # vector che results
mat <- c(88,91,69) # vector mat results

df <- data.frame(phy,che,mat) # create data frame objects

rownames(df) <- c("tom","dick","harry") # give names to the rows

print(df) # whole data frame

print(df[1,]) # row one
print(df[,1]) # col one

print(mtcars) # built in data frame

mtcarsmerge <- merge(mtcars, mtcars) # merge data frames

print(mtcarsmerge)

dfaddrow <- rbind(df,df)

print(dfaddrow)