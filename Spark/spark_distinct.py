from pyspark import SparkConf, SparkContext

def GetJobs(rec):
	record = rec.split("|")
	return(record[3])

conf = SparkConf()
sc = SparkContext(conf = conf)
rdd = sc.textFile("file:///home/cloudera/Users.txt")
rddjobs = rdd.map(GetJobs)
datajobsdistcount = rddjobs.distinct().count()
datajobscountbyval = rddjobs.countByValue()
print(datajobsdistcount)
print(datajobscountbyval)
