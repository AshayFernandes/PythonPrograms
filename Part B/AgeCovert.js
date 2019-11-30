function AgeConvert(DOB){
  var dat=DOB.split('-');
  var today=new Date();
  var presentdate=today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
  var presentdate=presentdate.split('-');
 
  var array=[];
  for(var i=0;i<3;i++){
  	array.push(Number(presentdate[i])-Number(dat[i]));
  }  
  console.log(array)
  var days=array[0]*365;
  if(array[1]<0){
    days=days-Math.abs(array[1])*30;
   }
  else
    days=days+array[1];

  if(array[2]<0)
  	 days=days-array[2];
  else
    days=days+array[2];	
 
 return days

}

var value=AgeConvert(prompt('enter age in YYYY-MM-DD format'));
alert('you are '+parseInt(value/365)+' years old');