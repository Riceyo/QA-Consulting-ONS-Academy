from pyspark import SparkConf, SparkContext

def GetMarks(x):
	split = x.split(",") # split the data up by comma
	return split[0], split[2] # remove the second unneeded column from the data so we can use map and reduce methods, note the index starts at zero

def SumMarks(a, b):
	return int(a) + int(b)

def PerMarks(x):
	return x * 100 / 300 # assumes we always have three marks for each student

conf = SparkConf()
sc = SparkContext(conf = conf)
rdd = sc.textFile("file:///home/cloudera/Results.txt")
rddencode = rdd.map(lambda x: x.encode("ascii", "ignore")) # encode unicode to ascii and ignore any errors
rddmarks = rddencode.map(GetMarks)
rddsummarks = rddmarks.reduceByKey(SumMarks) # create new rdd with key (student regno) and summed up marks for each key
rddpermarks = rddsummarks.mapValues(PerMarks) # create new rdd with key (student regno) and percentage calculated
data = rddpermarks.collect()
print data
