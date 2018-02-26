def odd_even():

	for i in range(0,2001):
		if (i % 2 == 1):
			print 'number is '+ str(i)+". This is an odd number"
		if (i % 2 == 0):
			print 'number is '+ str(i)+". This is an even number"
odd_even()