phy <- c(93,82,69) # vector phy results
che <- c(98,78,69) # vector che results
mat <- c(88,91,69) # vector mat results

res <- cbind(phy,che,mat) # create matrix object from vectors

print(res[1,1]) # row one and column one
print(res[1,]) # all columns
print(res[,1:2]) # all rows for columns one to two
print(res[1,c(1,3)]) # row one for columns one and three

colnames(res) <- c("phy","che","mat") # give names to the columns
rownames(res) <- c("tom","dick","harry") # give names to the rows

print(res["dick",]) # all of dick's results
print(res["harry","che"]) # harry's che result

print(colSums(res)) # add all columns
print(rowSums(res)) # add all rows

print(apply(res,2,mean)) # average the columns (1-row 2-col)

checkpass <- function(marks) # create function to check if passed
{
  markssummed <- base::sum(marks)
  if (((markssummed * 100) / 300) > 70)
    return("pass")
  else
    return("fail")
}

print(apply(res,1,checkpass)) # pass the values of the matrix rows to my checkpass function

print(attributes(res)) # attributes of the matrix
print(dim(res)) # dimentations of the matrix