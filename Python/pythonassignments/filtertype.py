#Assignment: Filter by Type

num = 10
name ='Albert'
lis =[1]
print type(lis)

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def filtbytype(x):
	if isinstance(x,int):
		if (x >=100):
			print("that's a big number!")
		else:
			print("that's a small number")

	if isinstance(x,str):
		if(len(x) >=50):
			print("long sentence")
		else:
			print("short sentence")
	if isinstance(x,list):
		if (len(x) >= 10):
			print("Big list!")
		else:
			print("Short list")

filtbytype(sI)
filtbytype(mI)
filtbytype(bI)
filtbytype(spI)
filtbytype(sS)
filtbytype(mS)
filtbytype(bS)
filtbytype(eS)
filtbytype(eS)
filtbytype(aL)
filtbytype(mL)
filtbytype(lL)
filtbytype(eL)
filtbytype(spL)
