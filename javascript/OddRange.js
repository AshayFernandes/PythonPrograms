function OddRange(num1,num2){
    od=[];
	 for(var i=num1;i<=num2;i++)
	 	{
          if(i%2!=0)
          	 od.push(i);
	 	} 
	 return od;	
}
num1=Number(prompt('enter the lower value in the range'));
num2=Number(prompt('enter the higher value'));
array=OddRange(num1,num2);

console.log('array');