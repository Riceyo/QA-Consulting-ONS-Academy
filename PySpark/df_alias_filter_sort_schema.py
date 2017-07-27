from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import *

conf = SparkConf()
sc = SparkContext(conf = conf)
sql = SQLContext(sc)

def splitrecord(rec):
	record=rec.split("|")
	return int(record[0]),int(record[1]),record[2],record[3],int(record[4])

rdd = sc.textFile("file:///home/cloudera/Users.txt")
rddheader = rdd.first() # create rdd of the header only
rddnoheader = rdd.filter(lambda line: line != rddheader) # create rdd with the header removed
rddsplit = rddnoheader.map(lambda x: x.encode("ascii", "ignore").split("|")) # convert data and split the data by pipe
df = sql.createDataFrame(rddsplit) # create data frame from rdd

df.show() # print the whole data frame
df.printSchema() # print the data frame schema
df.select("_2").show() # print only the second column
df.select(["_2", "_3"]).show() # print multiple columns
df.select(df._2.alias("Age"), df._3.alias("Gender")).show() # give the columns names
df.select(df._5, df._5 * 100).show() # calculation column
df.filter((df._2 < 25) & (df._3 == "M")).show() # filter data
df.filter((df._2 < 25) & (df._3 == "M")).select(df._4).show() # filter data and select specific column
df.sort(df._2.desc()).show() # order data by column

dfheader = sql.createDataFrame(rddsplit, ['id','age','gender','job','score']) # create data frame from rdd with header

dfheader.show() # print the whole data frame
dfheader.printSchema() # print the data frame schema
#----------------------
rddA= sc.textFile("file:///home/cloudera/Users.txt")
rddheader = rddA.first() # create rdd of the header only
rddnoheaderA = rddA.filter(lambda line: line != rddheader) # create rdd with the header removed
records=rddnoheaderA.map(splitrecord)
#------------------------
schema = StructType([
		StructField('id', LongType(), True)
		,StructField('age', LongType(), True)
		,StructField('gender', StringType(), True)
		,StructField('job', StringType(), True)
		,StructField('score', LongType(), True)
])

dfschemaheader = sql.createDataFrame(records, schema) # create data frame from rdd with header

dfcollect = df.select(["_2", "_3"]).collect() # collect data frame into list
dfschemaheader.printSchema()
dfschemaheader.show()
#print(dfcollect)
