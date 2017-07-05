ellipsis <- function(...)
  {
    print(paste(...))
    print(paste(min(...)))
    print(paste(max(...)))
  }

ellipsis(1,2,3,4,5)

ellipsislist <- function(...)
  {
    args = list(...)
    print(paste(args))
}

ellipsislist(1, 2, 3, "a","b","c","d","e", "list")

ellipsisvec <- function(...)
{
  vec = c(...)
  print(paste(vec))
}

ellipsisvec("a","b","c","d","e","vector")

atleasttwo <- function(a,b,...)
  {
    print(paste(a,b,...))
  }

atleasttwo(1,2)
atleasttwo(1,2,3)