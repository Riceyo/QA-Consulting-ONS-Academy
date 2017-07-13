from pyspark import SparkConf, SparkContext

def genre(x):
  genrenum[0] = genrenum[0] + int(x[5])
	genrenum[1] = genrenum[1] + int(x[6])
	genrenum[2] = genrenum[2] + int(x[7])
	genrenum[3] = genrenum[3] + int(x[8])
	genrenum[4] = genrenum[4] + int(x[9])
	genrenum[5] = genrenum[5] + int(x[10])
	genrenum[6] = genrenum[6] + int(x[11])
	genrenum[7] = genrenum[7] + int(x[12])
	genrenum[8] = genrenum[8] + int(x[13])
	genrenum[9] = genrenum[9] + int(x[14])
	genrenum[10] = genrenum[10] + int(x[15])
	genrenum[11] = genrenum[11] + int(x[16])
	genrenum[12] = genrenum[12] + int(x[17])
	genrenum[13] = genrenum[13] + int(x[18])
	genrenum[14] = genrenum[14] + int(x[19])
	genrenum[15] = genrenum[15] + int(x[20])
	genrenum[16] = genrenum[16] + int(x[21])
	genrenum[17] = genrenum[17] + int(x[22])
	genrenum[18] = genrenum[18] + int(x[23])
	return genrenum

conf = SparkConf()
sc = SparkContext(conf = conf)
rddmovies = sc.textFile("file:///home/cloudera/movie_data/Movies.item", 0)
rddratings = sc.textFile("file:///home/cloudera/movie_data/Moving-Ratings-Done.data", 0)
rddconvmovies = rddmovies.map(lambda x: x.encode("ascii", "ignore").split("|"))
rddconvratings = rddratings.map(lambda x: x.encode("ascii", "ignore").split("\t"))
genrenum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
datamoviesgenrenum = 	rddconvmovies.map(genre).collect()

print "unknown -", genrenum[]
print "action -", genrenum[]
print "adventure -", genrenum[]
print "animation -", genrenum[]
print "children's -", genrenum[]
print "comedy -", genrenum[]
print "crime -", genrenum[]
print "documentary -", genrenum[]
print "drama -", genrenum[]
print "fantasy -", genrenum[]
print "film-noir -", genrenum[]
print "horror -", genrenum[]
print "musical -", genrenum[]
print "mystery -", genrenum[]
print "romance -", genrenum[]
print "sci-fi -", genrenum[]
print "thriller -", genrenum[]
print "war -", genrenum[]
print "western -", genrenum[]
