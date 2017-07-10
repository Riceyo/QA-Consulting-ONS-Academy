from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
rdd = sc.parallelize(list)
datacount = rdd.count()
datacountbyval =  rdd.countByValue()
print(datacount)
for key in datacountbyval:
	print(key, "-", datacountbyval[key])