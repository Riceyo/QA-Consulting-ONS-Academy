from pyspark import SparkConf, SparkContext

conf = SparkConf()
sc = SparkContext(conf = conf)
rddmovies = sc.textFile("file:///home/cloudera/movie_data/Movies.item", 0)
rddratings = sc.textFile("file:///home/cloudera/movie_data/Moving-Ratings-Done.data", 0)
datamovies = rddmovies.map(lambda x: x.encode("ascii", "ignore").split("|")).collect()
dataratings = rddratings.map(lambda x: x.encode("ascii", "ignore").split("\t")).collect()

ratingcount5most = 0
ratingcount5mostmovie = ""

for moviesloop in datamovies: # loop the movies
	ratingcount5 = 0 # reset the rating 5 counter
	for ratingsloop in dataratings: # loop the ratings		
		if moviesloop[0] == ratingsloop[1]: # if the movie id matches in both data sets	
			if ratingsloop[2] == "5": # if a rating is 5
				ratingcount5 = ratingcount5 + 1 # add to the rating 5 counter
	if ratingcount5 > ratingcount5most: # keep a running total of the most ratings
		ratingcount5most = ratingcount5 
		ratingcount5mostmovie = moviesloop[1]

print ratingcount5mostmovie, ratingcount5most
