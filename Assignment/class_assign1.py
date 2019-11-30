
def list_string(st):
   temp=" "
   for i in st:
     temp+=i
   return temp
  
def ChangeString(value):
    newstring=[]  
    modified_string=[]    
    for i in value :
      if(i.isalpha()): 
        i=chr(ord(i) + 1)
        newstring.append(i)
      else:   
       newstring.append(i)
    for x in newstring:
       if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
          modified_string.append(x.upper())
       else:
          modified_string.append(x)
    return modified_string
                            

   
  
incremented_string=ChangeString("hello*3")


print(list_string(incremented_string))
   

