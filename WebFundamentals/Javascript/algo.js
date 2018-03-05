                                     //Chapter 1 Fundamentals

//Set MyNumber to 42, MyName to your name. Then swap MyNumber into MyName and vieversa.
 // var MyNumber = 42;
 // var MyName = 'Alberto';
 // var temp = MyNumber;
 // MyNumber = MyName;
 // MyName = temp;
 // console.log(MyName,MyNumber);
 // temp = MyNumber;
 // MyNumber = MyName;
 // MyName = temp;
 // console.log(MyName,MyNumber);

 //print -52 to 1066
 //print integers from -52 to 1066 using a FOR loop.

 // for (var i = -52; i<=1066; i++) {
 // 	console.log(i)
 // }

 //print all integers multiples of 5, from 512 to 4096. log how many there were.
// var count=0;
//  for (var i =512; i < 4096; i++) {
//  	if(i % 5 === 0){
//  		console.log(i);
//  		count = count+1;
//  	}
//  }
//  console.log(count);

//print multiples of 6 up to 60,000, using a WHILE loop
// var i = 6;
// while (i <= 60000)
// {
// 	if(i % 6 === 0){
// 		console.log(i);
// 	}
// 	i += 1;
// }

//Countdown
//  function countDown(int){
//  	var arr = [];
//  	for(var i = int; i >=0;i--){
//  		arr.push(i);
//  	}
//  	return arr;
//  }
//  countDown(8)
// console.log(countDown(8))

// print and return

// function printRet(arr){
// 	console.log(arr[0])
// 	return arr[1];
// }
// console.log(printRet([9,5]))

//Values greater than the second

// function greaterThanSecond(arr){
// 	var count =0;
// 	for(var i = 0; i<arr.length;i++){
// 		if(arr[i] > arr[1]){
// 			console.log(arr[i]);
// 			count = count + 1;
// 		}
// 	}
// 	return count;
// }
// console.log(greaterThanSecond([1,3,5,7,9,13]))

//Fit the first value

// function fitvalue(arr){
// 	for(var i = 0; i<arr.length;i++){
// 		if(arr[0] > arr.length){
// 			console.log('Too big!')
// 		}
// 		else if (arr[0]<arr.length){
// 			console.log('Too small')
// 		}
// 		else{
// 			console.log('Just Right')
// 		}
// 		break;
// 	}
// }
// console.log(fitvalue([8,3,5,7,9,13]))

//Biggie Size

// function biggieSize(arr){
// 	for(var i=0;i<arr.length;i++){
// 		if(arr[i]> 0){
// 			arr[i] = 'big';
// 		}
// 	}
// 	return arr;
// }
// console.log(biggieSize([-1,3,5,-5]))

// //reverse array

// function revArr(arr){
// 	var temp = 0;
// 	for(var i = 0; i< arr.length/2;i++){
// 		temp=arr[arr.length-1-i];
// 		arr[arr.length-1-i] = arr[i];
// 		arr[i]=temp;
// 	}
// 	return arr;
// }
// console.log(revArr([3,1,6,4,2]))

// function outlookNegative(arr){
// 	for(var i =0;i<arr.length;i++){
// 		if(arr[i]>0){
// 			arr[i] = -arr[i]
// 		}
// 	}
// 	return arr;
// }
// console.log(outlookNegative([1,-2,4,-5,7,3,-1]))

// // Only keep the last few
// //This one has not been yet solved

// function keepFew(arr,x){
// 	for (var i = arr.length; i >=0; i--) {
// 		arr.length = x;
// 	}
// 	return arr;
// }
// console.log(keepFew([2,4,6,8,10],3))

                                               //Chapter 2

 //Sigma

 function sigma(num){
 	sum = 0;
 	for(var i=0; i<= num;i++){
 		sum += i
 	}
 	return sum;
 }
 console.log(sigma(5))

 //factorial

  function factorial(num){
 	multiplication = 1;
 	for(var i=1; i<= num;i++){
 		multiplication *= i;
 	}
 	return multiplication;
 }
 console.log(factorial(5))