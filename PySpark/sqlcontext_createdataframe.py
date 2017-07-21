from pyspark import SparkConf, SparkContext, SQLContext

conf = SparkConf()
sc = SparkContext(conf = conf)
sql = SQLContext(sc)
rdd = sc.textFile("file:///home/cloudera/Users.txt")
rddheader = rdd.first()
rddnoheader = rdd.filter(lambda line: line != rddheader)
rddsplit = rddnoheader.map(lambda x: x.encode("ascii", "ignore").split("|"))
df = sql.createDataFrame(rddsplit)
df.show()
df.printSchema()
df.select("_2").show()
df.select(["_2", "_3"]).show()
