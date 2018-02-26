weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

# print weekend["Sun"]
# print capitals["svk"]

# for data in capitals:
# 	print data

# for key in capitals.iterkeys():
# 	print key

for val in capitals.itervalues():
	print val