#install.packages("RODBC")

require(RODBC)

conn <- odbcConnect("blah", uid="root", pwd="password")

df <- sqlQuery(conn, "select * from blah")

odbcCloseAll()

print(df)