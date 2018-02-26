var daysUntilMyBirthday = 60;

while (daysUntilMyBirthday >= 30){
	console.log(daysUntilMyBirthday, "days until my birthday. Such a long time...:("	);
	daysUntilMyBirthday = daysUntilMyBirthday -1;
}

while ( 30 > daysUntilMyBirthday && daysUntilMyBirthday >= 5){
	console.log(daysUntilMyBirthday, "days until my birthday. I'm so excited");
	daysUntilMyBirthday = daysUntilMyBirthday -1;
}
while (daysUntilMyBirthday < 5 && daysUntilMyBirthday > 0){
	console.log(daysUntilMyBirthday, "DAYS UNTIL MY BIRTHDAY!!!");
	daysUntilMyBirthday = daysUntilMyBirthday -1;
}

console.log("Have a party");