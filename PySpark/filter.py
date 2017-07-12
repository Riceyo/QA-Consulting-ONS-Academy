from pyspark import SparkConf, SparkContext

def overtenchecker(x):
	if x > 10:
		return True # true keeps element in new rdd
	else:
		return False # false removes element from new rdd

conf = SparkConf()
sc = SparkContext(conf = conf)
list = [1, 2, 3, 11, 12, 13]
rdd = sc.parallelize(list)
rddfilt = rdd.filter(overtenchecker) # run function on the rdd to filter elements into new rdd
data = rddfilt.collect()
print data
