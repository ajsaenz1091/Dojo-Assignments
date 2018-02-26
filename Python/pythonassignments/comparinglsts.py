list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

def comparelists(list1,list2):
	count = 0
	for idx in range(0,len(list1)):
		if (list1[idx]==list2[idx]):
			count+=1
				

	if (count == len(list1)):
		print('The lists are the same')
	else:
		print('the lists are not the same')
comparelists(list_one,list_two)
