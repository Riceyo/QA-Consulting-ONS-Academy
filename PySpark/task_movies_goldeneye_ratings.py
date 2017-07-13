from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
rddmovies = sc.textFile("file:///home/cloudera/movie_data/Movies.item", 0) # create movies rdd
rddratings = sc.textFile("file:///home/cloudera/movie_data/Moving-Ratings-Done.data", 0) # create ratings rdd
datamovies = rddmovies.map(lambda x: x.encode("ascii", "ignore").split("|")).collect() # encode, split, collect
dataratings = rddratings.map(lambda x: x.encode("ascii", "ignore").split("\t")).collect() #encode, split, collect

ratingcount5 = 0
ratingcount4 = 0
ratingcount3 = 0
ratingcount2 = 0
ratingcount1 = 0

for moviesloop in datamovies: # loop the movies
	for ratingsloop in dataratings: # loop the ratings
		if moviesloop[0] == ratingsloop[1]: # if the movie id matches in both data sets
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "5": # if goldeneye and 5 rating
				ratingcount5 = ratingcount5 + 1 # count 5 ratings
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "4": # if goldeneye and 4 rating
				ratingcount4 = ratingcount4 + 1 # count 4 ratings
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "3": # if goldeneye and 3 rating
				ratingcount3 = ratingcount3 + 1 # count 3 ratings
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "2": # if goldeneye and 2 rating
				ratingcount2 = ratingcount2 + 1 # count 2 ratings
			if moviesloop[1] == "GoldenEye (1995)" and ratingsloop[2] == "1": # if goldeneye and 1 rating
				ratingcount1 = ratingcount1 + 1 # count 1 ratings

print "5 -", ratingcount5
print "4 -", ratingcount4
print "3 -", ratingcount3
print "2 -", ratingcount2
print "1 -", ratingcount1
