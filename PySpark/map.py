from pyspark import SparkConf, SparkContext

def square(x):
	return x * x
	
def half(x):
	return x / 2

def oddoreven(x):
	if x % 2 == 0:
		 return("even")
	else:
		return("odd")

conf = SparkConf()
sc = SparkContext(conf = conf)
list = [1, 2, 3, 4, 5, 10, 20, 50]
rdd = sc.parallelize(list)
rddsquare = rdd.map(square) # apply function to each element in a new rdd (transform)
rddhalf = rdd.map(half) # apply function to each element in a new rdd (transform)
rddoddoreven = rdd.map(oddoreven)  # apply function to each element in a new rdd (transform)
datasquare = rddsquare.collect() # read the newly created rdd (action)
datahalf = rddhalf.collect() # read the newly created rdd (action)
dataoddoreven = rddoddoreven.collect() # read the newly created rdd (action)
print datasquare
print datahalf
print dataoddoreven
