from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
list = [1, 2, 3, 21, 22, 23]
rdd = sc.parallelize(list)
rddfilt = rdd.filter(lambda x: True if x > 10 else False)
data = rddfilt.collect()
print data
