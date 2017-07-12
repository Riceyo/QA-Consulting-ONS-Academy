from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
traineetuple = ((101, 'Richmond'), (102, 'Luke'), (103, 'David'))
trainertuple = ((101, 'Richmond'), (104, 'Binay'), (105, 'Anton'))
rddtrainees = sc.parallelize(traineetuple)
rddtrainers = sc.parallelize(trainertuple)
rddunion = rddtrainees.union(rddtrainers)
rddintersection = rddtrainees.intersection(rddtrainers)
rddsubtract = rddtrainees.subtract(rddtrainers)
dataunion = rddunion.collect()
dataintersection = rddintersection.collect()
datasubtract = rddsubtract.collect()
print dataunion
print dataintersection
print datasubtract
