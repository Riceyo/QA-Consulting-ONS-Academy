from pyspark import SparkConf, SparkContext

def GetMale(rec):
	record = rec.split("|")
	if record[2] == "M":
		return True
	else:
		return False

def GetFemale(rec):
	record = rec.split("|")
	if record[2] == "F":
		return True
	else:
		return False

conf = SparkConf()
sc = SparkContext(conf = conf)
rdd = sc.textFile("file:///home/cloudera/Users.txt") # read a text file
rddmale = rdd.filter(GetMale)
rddfemale = rdd.filter(GetFemale)
malecount = rddmale.count()
femalecount = rddfemale.count()
print "males -", malecount
print "females ", femalecount
