function isalpha(value){
	if(value.charCodeAt(0)>=65 && value.charCodeAt(0)<=90 || value.charCodeAt(0)>=97 && value.charCodeAt(0)<=122)
		return true;
	else
		 return false;
}


function LetterSurround(value){
       var i=0;
       var equ_count=0;
       if(isalpha(value[0]))
       	 return false;
       else{
             
            while(i<value.length)
            { 
       		  if(value[i]=='+'||value[i]=='='){

       		  	   if(value[i]=='='){
       		  	   	  equ_count=equ_count+1;
       		  	   	  i=i+1;
       		  	   	 continue;
       		  	   	}
       		  	   
       		  	   else{

                        if(isalpha(value[i+1])){
                     	   if(value[i+2]=='+'){
                     	  	  i=i+3;
                     	  	  continue;
                     	  	}                     	  
                     	   else
                     	  	 return false;

                        }
 					    else{
 					 	  i=i+1;
 					      continue;}	

       		  	    }
       		  	 }      

       		   else{
       		  	 i=i+1;
       		  	 continue;}
             }

        } 
        if(equ_count>0)
        	return true;
        else
        	return false;

       }	




var value=prompt('enter the string');
var result=LetterSurround(value);
if(result)
  alert('accepted');
else
  alert('not accepted');	
