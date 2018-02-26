
#Print odds

# for i in range(1,1001):
# 	print(i)
#print multiples of 5

'''for i in range(5,1000001):
	if(i % 5 == 0):
		print(i)'''

#sum List

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
	sum += i

print(sum)

#average list

a = [1, 2, 5, 10, 255, 3]
sum = 0
avg = 0

for i in a:
	sum += i
	avg = sum/len(a)

print(avg)