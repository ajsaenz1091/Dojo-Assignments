

//If you don't mind//

var hour= 8;
var minute=50;
var period ="am"

function theTime(hour,minute,period){
	if(minute > 30 && period === "am"){
			console.log("it's almost", hour +1,"in the morning");
		}
		else{
		console.log("it's just after", hour ,"in the evening");
	}
}

theTime (7,20,"pm");




