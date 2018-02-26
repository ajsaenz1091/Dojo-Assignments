def multiply(arr,num):
	a = [2,4,10,16]
	b = multiply(a,5)
   	 for x in arr:
        arr[x] *= num
    return arr
print multiply(a,b)
# output:
>>>[10,20,50,80]