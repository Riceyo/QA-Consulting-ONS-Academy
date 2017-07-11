from pyspark import SparkConf, SparkContext

def GetMarks(rec):
	record = rec.split(",")
	return record[0], record[2] # removes the subject columns

def SumMarks(a, b):
	return int(a) + int(b)

def PerMarks(x):
	return x * 100 / 300

conf = SparkConf()
sc = SparkContext(conf = conf)
rdd = sc.textFile("file:///home/cloudera/Results.txt")
rddencode = rdd.map(lambda x: x.encode("ascii", "ignore"))
rddmarks = rddencode.map(GetMarks)
rddsummarks = rddmarks.reduceByKey(SumMarks)
rddpermarks = rddsummarks.mapValues(PerMarks)
data = rddpermarks.collect()
print data
