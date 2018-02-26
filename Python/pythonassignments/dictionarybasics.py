personal = {"name":"Alberto",
			"age":"26",
			"country":"Costa Rica",
			"language":"Python"}

def dictionary(dic):
	for key in dic:
		newstr = "My " + key +": is "+dic[key]
		print newstr

dictionary(personal)