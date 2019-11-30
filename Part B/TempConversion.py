# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:56:07 2019

@author: Ashay Fernandes
"""

lyst1=[]
def celTOkel():
    value=float(input('enter the value'))
    result=float(value+273.15)
    tup=("from celcius:",value,"to-kelvin:",result)
    lyst1.append(tup)
    
def celTOfah():
    value=float(input('enter the value'))
    result=float((value*9/5)+32)    
    tup=("from celsisus:",value,"To-fah:",result)
    lyst1.append(tup)
    
def kelTOfah():
   value=float(input('enter the value'))
   result=float(((value-273.15)*9/5) +32)
   tup=("from kelvin:",value,'to fah:',result)
   lyst1.append(tup)

def TO_FROM():
   revlyst=[] 
   for i in range(0,len(lyst1)):
       lyst2=[x for x in list(lyst1[i])]
       lyst2.reverse()
       j=lyst2[0]
       temp=lyst2[1]
       lyst2[1]=j
       lyst2[0]=temp
       j=lyst2[3]
       temp=lyst2[2]
       lyst2[2]=j
       lyst2[3]=temp
       revlyst.append(tuple(lyst2))
   print(revlyst)

while True:
  print('enter \n1:to convert from celsius to kelvin \n2:to convert from celsius to fahrenheit \n')
  print('3:convert from kelvin to fahrenheit\n4:to display values from -to-values\n5:to display values to-from\n6:exit')
  num=int(input())
  if num==1 :
      celTOkel()
  elif num==2:
      celTOfah()
  elif num==3:
      kelTOfah()
  elif num==4:
      print(lyst1)
  elif num==5:    
      TO_FROM()
  elif num==6:
      break
  else:
      print('invalid command')
      
       
       