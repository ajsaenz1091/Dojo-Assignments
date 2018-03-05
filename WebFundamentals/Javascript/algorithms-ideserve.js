// Find the last index of an element in a sorted array with duplicates
var x = [0,1,2,2,4,5,5,5,8];
function indexDup(arr) {
	for(var i=arr.length-1;i>=0;i--){
		if(arr[i]===arr[i+1]){
			console.log(i+1);
			break;
		}
	}
}
indexDup(x)
