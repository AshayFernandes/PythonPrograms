# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:38:17 2019

@author: Ashay Fernandes
"""

def LetterSurround(value):
    eqcount=0
    flag=0
    if value[0]=='+' or value[0]=='=':
        i=0
        while i < len(value):
            if value[i].isalpha():
                return False
            if value[i]=='=':
                eqcount=eqcount+1
            elif value[i]=='+':
               if i+1 < len(value) and i+2 < len(value): 
                if value[i+1].isalpha() and value[i+2]=='+':
                    i=i+3
               else:
                 return False  
            i=i+1
        
        if flag==0 and eqcount>0: 
          return True 
        return False  
    else:
        return False 
    
value=LetterSurround(input('enter the string'))
if(value):
  print('Accepted')
else:
  print('Not Accepted')    
                    