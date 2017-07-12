from pyspark import SparkConf, SparkContext

def Add(num1, num2):
	return num1 + num2

conf = SparkConf()
sc = SparkContext(conf = conf)
numlist = [1, 2, 3, 4, 5]
rdd = sc.parallelize(numlist)
data = rdd.reduce(Add) # apply function to all elements accumulatively
print data
