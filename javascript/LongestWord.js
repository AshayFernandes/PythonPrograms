
function word(){
  var length=0;
  var words=''; 	
  var tag=document.getElementById('text');
  var text=tag.value;
  
  var array=text.split(" ");
  
   array.forEach(function(value){
     
          if(value.length>length){
          	length=value.length;
          	words=value;
          }


   });
   alert('length of the longest word is '+length+' and the word is '+words);
 }

