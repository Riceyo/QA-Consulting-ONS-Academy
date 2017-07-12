from pyspark import SparkConf, SparkContext # import spark modules

conf = SparkConf() # create spark config object
sc = SparkContext(conf = conf) # create main spark object passing it the config object
list = [1, 2, 3, 4, 5] # create some data
rdd = sc.parallelize(list) # create the rdd (sends the data out to the nodes in the cluster)
data = rdd.collect() # read the data from rdd (action method)
for x in data: # loop the data
	print x # print the data
