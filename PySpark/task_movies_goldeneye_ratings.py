from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
rddmovies = sc.textFile("file:///home/cloudera/movie_data/Movies.item", 0)
rddratings = sc.textFile("file:///home/cloudera/movie_data/Moving-Ratings-Done.data", 0)
datamovies = rddmovies.map(lambda x: x.encode("ascii", "ignore").split("|")).collect()
dataratings = rddratings.map(lambda x: x.encode("ascii", "ignore").split("\t")).collect()

ratingcount5 = 0
ratingcount4 = 0
ratingcount3 = 0
ratingcount2 = 0
ratingcount1 = 0

for moviesloop in datamovies:
	for ratingsloop in dataratings:
		if moviesloop[0] == ratingsloop[1]:
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "5":
				ratingcount5 = ratingcount5 + 1
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "4":
				ratingcount4 = ratingcount4 + 1
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "3":
				ratingcount3 = ratingcount3 + 1
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "2":
				ratingcount2 = ratingcount2 + 1
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "1":
				ratingcount1 = ratingcount1 + 1

print "5 -", ratingcount5
print "4 -", ratingcount4
print "3 -", ratingcount3
print "2 -", ratingcount2
print "1 -", ratingcount1
