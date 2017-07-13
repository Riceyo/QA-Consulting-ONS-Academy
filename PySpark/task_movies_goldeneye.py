from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
rddmovies = sc.textFile("file:///home/cloudera/movie_data/Movies.item", 0)
rddratings = sc.textFile("file:///home/cloudera/movie_data/Moving-Ratings-Done.data", 0)
datamovies = rddmovies.map(lambda x: x.encode("ascii", "ignore").split("|")).collect()
dataratings = rddratings.map(lambda x: x.encode("ascii", "ignore").split("\t")).collect()
#datamovies = rddconvmovies.collect()
#dataratings = rddconvratings.collect()

ratingcount = 0
for moviesloop in datamovies:
	for ratingsloop in dataratings:
		if moviesloop[0] == ratingsloop[1]:
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "5":
				ratingcount = ratingcount + 1
print ratingcount