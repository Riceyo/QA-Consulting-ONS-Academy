from pyspark import SparkConf, SparkContext

def GetMale(x):
	split = x.split("|") # split the rows data by pipe
	if split[2] == "M":
		return True
	else:
		return False

def GetFemale(x):
	split = x.split("|") # split the rows data by pipe
	if split[2] == "F":
		return True
	else:
		return False

conf = SparkConf()
sc = SparkContext(conf = conf)
rdd = sc.textFile("file:///home/cloudera/Users.txt") # read text file into an rdd row by row, but does not split the rows values
rddmale = rdd.filter(GetMale)
rddfemale = rdd.filter(GetFemale)
malecount = rddmale.count()
femalecount = rddfemale.count()
print "males -", malecount
print "females -", femalecount
