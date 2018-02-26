var p=1;
var reward = 0;

for (var d = 1; d <= 30; d++) {
	p *= 2;
	reward = p * 0.01;
}

console.log(reward);
