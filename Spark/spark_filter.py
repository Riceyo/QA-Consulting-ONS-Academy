from pyspark import SparkConf, SparkContext

def overtenchecker(x):
	if x > 10:
		return True
	else:
		return False

conf = SparkConf()
sc = SparkContext(conf = conf)
list = [1, 2, 3, 11, 12, 13]
rdd = sc.parallelize(list)
rddfilt = rdd.filter(overtenchecker) # filter rdd elements into new rdd
data = rddfilt.collect()
print(data)