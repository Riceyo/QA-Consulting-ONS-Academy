from pyspark import SparkConf, SparkContext

def SalaryBonus(rec):
	if rec < 20000:
		return rec + 100
	else:
		return rec + 200

conf = SparkConf()
sc = SparkContext(conf = conf)
salaries = [['rich',19000],['luke',21000],['dave',22000]]
rdd = sc.parallelize(salaries)
rddnewsal = rdd.mapValues(SalaryBonus)
data = rddnewsal.collect()
print(data)
