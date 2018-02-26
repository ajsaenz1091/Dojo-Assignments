
#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# # input
# 2 = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"


def typeList(x):
	newstr = ''
	count = 0

	for i in x:	
		if isinstance(i,str):
			newstr += i
			newstr += ' '
		if isinstance(i,int) or isinstance (i,float):
			count += i
	if (count > 0 and len(newstr) > 0):
	    print("The list you entered is of mixed type")
	    print(newstr)
	    print(count)
	elif (count > 0):
		print("The list you entered is of integer type")
		print(count)
	else:
		print("The list you entered is of integer type")
		print(count)
typeList(l)



	



typeList(l)


