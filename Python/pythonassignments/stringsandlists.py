
#find and replace
words = "It's thanksgiving day. It's my birthday, too!"
print(words.find("day"))
words2 = words.replace("day", "month")
print(words2)

#Min and Max
x = [2,54,-2,7,12,98]

print(min(x))
print(max(x))

#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
list = [x[0],x[len(x)-1]]
print(x[0],x[len(x)-1])
print(list)

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
print(x)
x2=[]
x3=[]
for i in range(0,len(x)/2):
	x2.append(x[i])
for i in range(len(x)/2, len(x)):
    x3.append([i])	

x3.insert(0, x2)

print(x3)





