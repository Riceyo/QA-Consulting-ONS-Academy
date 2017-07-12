from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
traineetuple = ((101, 'Richmond'), (102, 'Luke'), (103, 'David')) # data set shapes must be the same for these methods
trainertuple = ((101, 'Richmond'), (104, 'Binay')) # data set shapes must be the same for these methods
rddtrainees = sc.parallelize(traineetuple)
rddtrainers = sc.parallelize(trainertuple)
rddunion = rddtrainees.union(rddtrainers) # union the data sets, return everything
rddintersection = rddtrainees.intersection(rddtrainers) # intersect the data sets, return the duplicates once but nothing else
rddsubtract = rddtrainees.subtract(rddtrainers) # subtract the data sets, return everything except for the duplicates
dataunion = rddunion.collect()
dataintersection = rddintersection.collect()
datasubtract = rddsubtract.collect()
print dataunion
print dataintersection
print datasubtract
