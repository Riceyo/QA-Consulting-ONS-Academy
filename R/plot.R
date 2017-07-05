# print(OrchardSprays)

# View(OrchardSprays)

# print(max(OrchardSprays["decrease"]))

print(OrchardSprays[which.max(OrchardSprays$decrease),])

plot(OrchardSprays$treatment, OrchardSprays$decrease,
     col="red", main='blah')

ggplot(main='blah'
       ,data=OrchardSprays
       ,aes(x=treatment, y=decrease)) +
        geom_boxplot(color="red", fill="orange", alpha=0.4)