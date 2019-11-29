function check(){
	var tag=document.getElementById('first');
	var value=tag.value;
	var re=/[0-9]+/;
	 return re.test(value);
}

function result(){
	var tag=document.getElementById('first');
	var value=tag.value;
	document.getElementById('res').innerHTML=Number(value)*2;
	
}

function result1(){
	var tag=document.getElementById('first');
	var value=tag.value;
	document.getElementById('res').innerHTML=Number(value)*Number(value);

}
