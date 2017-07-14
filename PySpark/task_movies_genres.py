from pyspark import SparkConf, SparkContext

genreunknown = 0
genreaction = 0
genreadventure = 0
genreanimation = 0
genrechildrens = 0
genrecomedy = 0
genrecrime = 0
genredocumentary = 0
genredrama = 0
genrefantasy = 0
genrefilmnoir = 0
genrehorror = 0
genremusical = 0
genremystery = 0
genreromance = 0
genrescifi = 0
genrethriller = 0
genrewar = 0
genrewestern = 0

conf = SparkConf()
sc = SparkContext(conf = conf)
rddmovies = sc.textFile("file:///home/cloudera/movie_data/Movies.item", 0)
rddconvmovies = rddmovies.map(lambda x: x.encode("ascii", "ignore").split("|"))
datamovies = rddconvmovies.collect()

for moviesloop in datamovies: # loop the movies
	genreunknown = genreunknown + int(moviesloop[5])
	genreaction = genreaction + int(moviesloop[6])
	genreadventure = genreadventure + int(moviesloop[7])
	genreanimation = genreanimation + int(moviesloop[8])
	genrechildrens = genrechildrens + int(moviesloop[9])
	genrecomedy = genrecomedy + int(moviesloop[10])
	genrecrime = genrecrime + int(moviesloop[11])
	genredocumentary = genredocumentary + int(moviesloop[12])
	genredrama = genredrama + int(moviesloop[13])
	genrefantasy = genrefantasy + int(moviesloop[14])
	genrefilmnoir = genrefilmnoir + int(moviesloop[15])
	genrehorror = genrehorror + int(moviesloop[16])
	genremusical = genremusical + int(moviesloop[17])
	genremystery = genremystery + int(moviesloop[18])
	genreromance = genreromance + int(moviesloop[19])
	genrescifi = genrescifi + int(moviesloop[20])
	genrethriller = genrethriller + int(moviesloop[21])
	genrewar = genrewar + int(moviesloop[22])
	genrewestern = genrewestern + int(moviesloop[23])

print "unknown -", genreunknown
print "action -", genreaction
print "adventure -", genreadventure
print "animation -", genreanimation
print "children's -", genrechildrens
print "comedy -", genrecomedy
print "crime -", genrecrime
print "documentary -", genredocumentary
print "drama -", genredrama
print "fantasy -", genrefantasy
print "film-noir -", genrefilmnoir
print "horror -", genrehorror
print "musical -", genremusical
print "mystery -", genremystery
print "romance -", genreromance
print "sci-fi -", genrescifi
print "thriller -", genrethriller
print "war -", genrewar
print "western -", genrewestern
