#Step:1 Creating List

MyFavMovies = ["Batman triology","Intersteller","Inception","DDLJ"]

print(MyFavMovies)
for movies in MyFavMovies:
    print(movies)


if "DDLJ" in MyFavMovies:
    print("DDLJ is part of your Movies List ")
    #part of it
    #part it
#Out scope

MyFavMovies[2]= "Hero No 1"
MyFavMovies[3]= "Hero No 1"
for movies in MyFavMovies:
    print(movies)

print(MyFavMovies[1])
