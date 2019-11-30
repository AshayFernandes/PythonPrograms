def LetterSurround(value):
    for x in range(0,len(value)-1):
       if( x==0 and value[x].isalpha()):
         return False
  
       if(value[x]=='+' or value[x]=='='):
          if(value[x]=='='):
            continue
          else:
            if(value[x+1].isalpha()):
                if(value[x+2]=='+'):
                   x=x+2
            elif(value[x+1]=='+' or value[x+1]=='=' or not(value[x+1].isalpha())):
               continue
            else:
                return False
        
    return True     
       
num=LetterSurround('+d+=3=+s+')

if(num):
  print('accepted')
else:
  print('rejected')            
          
           
