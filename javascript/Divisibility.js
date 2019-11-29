function check(){
 var tag=document.getElementsByTagName('input')[0];

 var value=parseInt(tag.value);
 
 var re=/[0-9]+/;
  return re.test(value);

}

function result(){
	var tag=document.getElementsByTagName('input')[0];
 var value=Number(tag.value);
	if(value%3==0 || value%7==0)
 	 alert('The number is divisible by 3 or 7');
 else
   alert('the number is not divisible by 3 or 7');
}