# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:07:26 2019

@author: Ashay Fernandes
"""

def Oddrange(num1,num2):
    lyst=[]
    for x in range(num1,num2+1):
        if (x%2)!=0:
            lyst.append(x)
    return(lyst)        
            
    
num1=int(input('enter the lower number'))
num2=int(input('enter the higher number'))

lyst1=Oddrange(num1,num2)

print("the odd number range is")
print(lyst1)    