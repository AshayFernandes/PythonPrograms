function HourMinute(value){

	var hour=parseInt(value/60);
	var minutes=value%60;
	alert(hour+':'+minutes); 
}

HourMinute(Number(prompt('enter the number of minutes')));