from pyspark import SparkConf, SparkContext

def SalaryBonus(x):
	if x < 20000:
		return x + 100
	else:
		return x + 200

conf = SparkConf()
sc = SparkContext(conf = conf)
salaries = [['Richmond', 19000], ['Luke', 21000], ['David', 22000]]
rdd = sc.parallelize(salaries)
rddnewsal = rdd.mapValues(SalaryBonus) # apply function to every value in the rdd
data = rddnewsal.collect()
print data
