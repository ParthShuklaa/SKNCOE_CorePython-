MyWatches = ("Rolex","Armani","Titan", "Rolex")

def Display():
    for watches in MyWatches:
        print(watches)


#MyWatches[1] = "Maxima" # Not Allowed

Display()

print(MyWatches.count("Rolex"))
#Counts occurence of a particular element