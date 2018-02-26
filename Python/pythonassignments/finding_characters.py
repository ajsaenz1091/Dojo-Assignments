
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']


def findchar(list1,char):
	count = 0
	newlist = []
	for idx in list1:
		for i in idx:
			if (i == char):
				newlist.append(idx)
	print(newlist)
findchar(word_list,'o')


