dfcars <- rxImport("c://cars.sas7bdat")

print(cars)

carsasiareardrive <- sum(dfcars$Origin == "Asia" & dfcars$DriveTrain == "Rear")
dfcarseuro <- dfcars[which(dfcars$Origin == "Europe"),]
dfcarsusa <- dfcars[which(dfcars$Origin == "USA"),]
carseuroavgbhp <- round(mean(dfcarseuro$Horsepower))
carsusaavgprice <- round(mean(dfcarsusa$MSRP))
dfcars["pricebhpratio"] <- dfcars$MSRP / dfcars$Horsepower # add column to data frame for price / horsepower ratio

#print(dfcars)
print(paste("cars asia rear drive count:", carsasiareardrive))
print(paste("cars euro avg bhp:", carseuroavgbhp))
print(paste("cars usa avg price:", carsusaavgprice))
print("cars avg price / bhp ratio by region:")
print(aggregate(x=dfcars$pricebhpratio, by=list(Region = dfcars$Origin), FUN = mean)) # average price / bhp ratio by region
