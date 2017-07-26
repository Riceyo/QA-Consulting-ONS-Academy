csv = read.csv("c:\\piratebay.csv")

df <- data.frame(csv)

df["pop"] <- df$seeders + df$leechers # add column to data frame that sums seeders and leechers
df["ratio"] <- df$seeders / df$leechers # add column to data frame that works out seeder to leecher ratio

dfpoporder <- df[order(-df$pop),] # create new data frame ordered by pop column
dfseedorder <- df[order(-df$seeders),] # create new data frame ordered by seeders column
dfleechorder <- df[order(-df$leechers),] # create new data frame ordered by leechers column
dfratioorder <- df[order(-df$ratio),] # create new data frame ordered by ratio column
dfsizeorder <- df[order(-df$size),] # create new data frame ordered by ratio column
deadtorrentcount <- length(which(df$seeders == 0) | which(df$leechers == 0)) # count amount of dead torrents
dfdeadremoved <- df[!df$seeders == 0 | !df$leechers == 0,] # create new data frame with dead torrents removed

print(paste("most popular torrentid:", dfpoporder[1,1]))
print(paste("most seeded torrentid:", dfseedorder[1,1]))
print(paste("most leeched torrentid:", dfleechorder[1,1]))
print(paste("highest ratio torrentid:", dfratioorder[1,1]))
print(paste("largest torrentid:", dfsizeorder[1,1]))
print(paste("dead torrent count:", deadtorrentcount))

plot(df$size, df$pop, pch=21, col="red", bg="yellow"
     ,main="torrent data", sub="size to popularity"
     ,xlab="size", ylab="popularity"
     ,xlim=c(1000, dfsizeorder[1,1]*100/90), ylim=c(10, 2000))

plot(df$size, df$category, pch=21, col="red", bg="yellow"
     ,main="torrent data", sub="category to popularity"
     ,xlab="category", ylab="popularity")
