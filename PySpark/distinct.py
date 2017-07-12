from pyspark import SparkConf, SparkContext

def GetJobs(rec):
	record = rec.split("|")
	return(record[3])

conf = SparkConf()
sc = SparkContext(conf = conf)
rdd = sc.textFile("file:///home/cloudera/Users.txt")
rddjobs = rdd.map(GetJobs)
rddjobsheader = rddjobs.first()
rddjobsfilthead = rddjobs.filter(lambda line: line != rddjobsheader)
datajobsdistcount = rddjobs.distinct().count()
datajobscountbyval = rddjobs.countByValue()
datajobsfiltheadcountbyval = rddjobsfilthead.countByValue()
print datajobsdistcount
print datajobscountbyval
for x in datajobscountbyval:
	print x, datajobscountbyval[x]
for x in datajobsfiltheadcountbyval:
	print x, datajobsfiltheadcountbyval[x]
