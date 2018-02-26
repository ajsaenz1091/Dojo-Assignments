


for idx in range(0,8):
	newstr=''
	for idx1 in range(0,8):
		if ((idx1 + idx) % 2 == 0):
			newstr += "*"
		else:
			newstr+= ' '
	print newstr


