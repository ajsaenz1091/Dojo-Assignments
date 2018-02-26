
#part one
x=[4,6,1,3,5,7,25]
y=[4,6,1,6,5,7,29]
def draw_stars(list1):
	for i in list1:
		newstr = ''
		for j in range(0,i):
			newstr += '*'
		print newstr
draw_stars(x)

#part two
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(list1):
	for i in list1:
		newstr = ''
		if (isinstance(i,str)):
			for z in range(0, len(i)):
				newstr += i[0].lower()
			print newstr
		else:
			for j in range(0,i):
				newstr += '*'
			print newstr
draw_stars(x)
