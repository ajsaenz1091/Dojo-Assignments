function Dubleup(arr){
var origLen = arr.length;
arr.length = arr.length*2;//3
for (var i= origLen-1;i >=0; i--){
    arr[i*2] = arr[i];
    arr[i*2+1] = arr[i];
}
return arr;
}

console.log(DoubleUp([7,4,10]))



//0 1 2 3 4 5
// 7 4 10
// 7 4 10 ? 10 10