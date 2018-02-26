print "Hello World!"


def geteven():
	sum = 0
	for i in range(1,1001):
		if i % 2 == 0:
			sum += i	
	return sum

print geteven()		

def sumodd():
	sum =0
	for i in range(1,5001):
		if i % 2 ==1:
			sum += i
	return sum
print sumodd()

def iterArr(arr):
	sum = 0
	for i in arr:
		sum += i
	return sum

print iterArr([1,2,3,4,5,6,7,8,9])

def findMax(arr):
	return max(arr)
print findMax([1,2,3,4,5,6,7,8,9])

def findAvg(arr):
	sum = 0
	for i in arr:
		sum += i 
	avg = sum / len(arr)
	return avg
print findAvg([1,2,3,4,5,6,7,8,9])


def arrOdd():
	newarr = []
	for i in range(1,51):
		if i % 2 ==1:
			newarr.append(i)
	return newarr
print arrOdd()

def greaterY(arr,Y):
	count = 0
	for i in arr:
		if i > Y:
			count += 1
	return count
print greaterY([1,2,3,4,5,6,7,8,9],5)

def squareVal(arr):
	for idx,val in arr:


#swap out negatives
def swapNegatives(arr):
	for idx in range(0,len(arr)):
		if arr[idx] < 0:
			arr[idx]="Dojo"
	print arr
x =[1,2,-13,-12,42,-9]
swapNegatives(x)

# shift array values 

x = [12,13,42,95]
def shiftLeft(arr):
	for idx in range(0,len(arr)-1):
		arr[idx] = arr[idx] +1
	arr[len(arr)-1]=0
	print arr
shiftLeft(x)







