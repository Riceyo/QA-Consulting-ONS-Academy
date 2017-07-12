from pyspark import SparkConf, SparkContext

def SplitPer(x):
	split = x.split(",")
	return split[0], split[1], split[2]

def SplitRes(x):
	split = x.split(",")
	return split[0], split[2]

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
rddperhead = rddper.first()
rddreshead = rddres.first()
rddperremhead = rddper.filter(lambda line: line != rddperhead)
rddresremhead = rddres.filter(lambda line: line != rddreshead)
rddpersplit = rddperremhead.map(SplitPer)
rddressplit = rddresremhead.map(SplitRes)	
rddresadd = rddressplit.reduceByKey(Add)
dataper = rddpersplit.collect()
datares = rddressplit.collect()
dataresadd = rddresadd.collect()
print dataper
print datares
print dataresadd
for resloop in dataresadd:
	for perloop in dataper:
		if perloop[0] == resloop[0]:
			count = len(perloop[0])
			percent = resloop[1] * 100 / int(str(count) + '00')
			grade = CalcGrade(percent)
			print ''
			print 'student reg number:', perloop[0]
			print 'student name:', perloop[1]
			print 'exams taken:', count
			print 'percentage:', percent, '%'
			print 'grade:', grade
