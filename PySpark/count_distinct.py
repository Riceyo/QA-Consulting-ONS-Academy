from pyspark import SparkConf, SparkContext

def GetJobs(x):
	split = x.split("|")
	return split[3]

conf = SparkConf()
sc = SparkContext(conf = conf)
rdd = sc.textFile("file:///home/cloudera/Users.txt")
rddjobs = rdd.map(GetJobs)
rddjobsheader = rddjobs.first()
rddjobsfilthead = rddjobs.filter(lambda line: line != rddjobsheader)
datajobsdistcount = rddjobs.distinct().count() # return count of unique rows in the rdd
datajobscountbyval = rddjobs.countByValue()
datajobsfiltheadcountbyval = rddjobsfilthead.countByValue()
print datajobsdistcount
print datajobscountbyval
for x in datajobscountbyval:
	print x, datajobscountbyval[x]
for x in datajobsfiltheadcountbyval:
	print x, datajobsfiltheadcountbyval[x]
