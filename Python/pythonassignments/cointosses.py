import random
def coinToss():
	head_count = 0;
	tail_count =0;
	toss_count =0;

	for x in range(1,5001):
		toss = round(random.random())
		if toss == 0:
			head_count += 1
			toss_count += 1
			print "Attempt#", toss_count ,": Throwing a coin... It's head! ...Got " , "head(s) so far and"
		else:
			tail_count += 1
			toss_count += 1
			print "Attempt#", toss_count ,": Throwing a coin... It's tail! ...Got " , "head(s) so far and"
coinToss()
