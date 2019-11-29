# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:14:08 2019

@author: Ashay Fernandes
"""

def ChangeString(value):
     lyst=[]
     for i in range(0,len(value)):
        if value[i].isalpha():
            if ord(value[i])==90:
                lyst.append(chr(65))
            elif(ord(value[i])==122):
                lyst.append(chr(97))
            else:    
                lyst.append(chr(ord(value[i])+1))      
        else:
            lyst.append(value[i])
            
     newlyst=[]
     for i in range(0,len(lyst)):
         if (lyst[i]=='a' or lyst[i]=='e' or lyst[i]=='i' or lyst[i]=='o' or lyst[i]=='u'):
            newlyst.append(lyst[i].upper())
         else:
            newlyst.append(lyst[i])
     string=''
     for x in newlyst:
         string=string+x
     return string    
         
 
print(ChangeString(input('enter the string')))    