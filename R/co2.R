print(CO2)

class(CO2$Type)

print(mean(CO2$uptake))

plot(CO2$Type, CO2$uptake)

quebec_CO2 <- (CO2[which(CO2$Type == "Quebec"),])

mississippi_CO2 <- (CO2[which(CO2$Type == "Mississippi"),])

print(quebec_CO2)

print(mississippi_CO2)

Create a function called mean_checker that will take in 2 vectors, give you the mean of
both, then which has the higher mean. Run it to find out whether Mississippi or
Quebec has the higher uptake. 