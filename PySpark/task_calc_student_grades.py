from pyspark import SparkConf, SparkContext

def SplitPer(x):
	split = x.split(",")
	return split[0], split[1], split[2]

def SplitRes(x):
	split = x.split(",")
	return split[0], split[2] # only keep the student regno (key) and their marks data so we can use the reducebykey method to sum their marks

def Add(x, y):
	return int(x) + int(y)

def CalcGrade(x):
	if x > 89:
		return 'A+'
	if x > 79 and x < 90:
		return 'A'
	if x > 69 and x < 80:
		return 'B'
	if x > 59 and x < 70:
		return 'C'
	if x < 60:
		return 'Fail'

conf = SparkConf()
sc = SparkContext(conf = conf)
rddper = sc.textFile("file:///home/cloudera/student_perinfo.csv", 0)
rddres = sc.textFile("file:///home/cloudera/student_results.csv", 0)
rddperhead = rddper.first() # get the header (first row) from the student personal info data
rddreshead = rddres.first() # get the header (first row) from the student results data
rddperremhead = rddper.filter(lambda line: line != rddperhead).map(lambda x: x.encode("ascii", "ignore")) # remove header from the data and encode
rddresremhead = rddres.filter(lambda line: line != rddreshead).map(lambda x: x.encode("ascii", "ignore")) # remove header from the data and encode
rddpersplit = rddperremhead.map(SplitPer) # split the data
rddressplit = rddresremhead.map(SplitRes) # split the data
rddresadd = rddressplit.reduceByKey(Add) # sum the students marks
dataper = rddpersplit.collect()
datares = rddressplit.collect()
dataresadd = rddresadd.collect()
datarescount = rddressplit.countByKey() # count how marks we have for the student
bestpercent = 0
for resloop in dataresadd: # loop the student results summed up data
	for perloop in dataper: # loop the student personal info data
		if perloop[0] == resloop[0]: # if the regno match
			count = datarescount[perloop[0]] # count how many marks we have for the student
			percent = resloop[1] * 100 / int(str(count) + '00') # calculate their percentage based on how many marks we have for them
			grade = CalcGrade(percent) # calculate their grade based on their percent
			if percent > bestpercent:
				bestpercent = percent
				beststudent = perloop[1]
			print ""
			print "student reg number:", perloop[0]
			print "student name:", perloop[1]
			print "exams taken:", count
			print "percentage:", percent, "%"
			print "grade:", grade
print ""
print "best student:", beststudent
