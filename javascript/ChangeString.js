function ChangeString(value){
   var string='';
   var string1='';
   var n;
	for(var i=0;i<value.length;i++)
	{
		if(value.charCodeAt(i)>=65 && value.charCodeAt(i)<=90 || value.charCodeAt(i)>=97 && value.charCodeAt(i)<=122){
			if(value.charCodeAt(i)==90)
                 string+=String.fromCharCode(65);
             else if(value.charCodeAt(i)==122)
             	 string+=String.fromCharCode(97);
             else{
             	n=value.charCodeAt(i)+1;

             	string+=String.fromCharCode(n);
             }
           	
		}
		  else
          string+=value[i];  
	}
	
	for(var i=0;i<string.length;i++)
      {
      	 if(string[i]=='a'||string[i]=='e'||string[i]=='i'||string[i]=='o'||string[i]=='u'){
      	 	string1+=string[i].toUpperCase();
      	 }
      	 else
      	 	string1+=string[i]; 

      }
      alert(string1);
}

ChangeString(prompt('enter the string'));

