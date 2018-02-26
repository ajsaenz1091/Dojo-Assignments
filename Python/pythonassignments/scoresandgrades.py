import random
def scoresAndGrades():

	score = []

	for idx in range(0,10):
	    score.append(random.randint(60,100))  

	for num in score:

		if (60<=num<=69):
			print("Score:" +str(num)+"; Your grade is D")
		elif (70<=num<=79):
			print("Score:" +str(num)+"; Your grade is C")
		elif (80<=num<=89):
			print("Score:" +str(num)+"; Your grade is B")
		elif (num >=90):
			print("Score:" +str(num)+"; Your grade is A")

scoresAndGrades()