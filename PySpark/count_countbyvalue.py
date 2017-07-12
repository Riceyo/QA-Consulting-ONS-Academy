from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
rdd = sc.parallelize(list)
datacount = rdd.count() # count values in rdd
datacountbyval =  rdd.countByValue() # count occurrences of values in rdd
print(datacount)
for x in datacountbyval:
	print x, "-", datacountbyval[x]
