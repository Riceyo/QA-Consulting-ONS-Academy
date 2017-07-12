from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
list = [1,2,3,4,5,6,7,8,9,10,11,12]
rdd = sc.parallelize(list, 3) # partition 
rdd.saveAsTextFile("file:///home/cloudera/test/")
