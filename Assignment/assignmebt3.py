# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:49:29 2019

@author: Ashay Fernandes
"""

"""
q> write a temperature converter python progra which is menu driven each such conversion logic
   should be defined in seperate functions.The program should call the respective function based on the users
   's requirement.the program should run as long as the user wishes so.provide an option to view the conversion
    stored as list of tuples with attributes from unit value to unit value sorted by the users choice"""
    
    
lyst1=[]
def celtokel():
    num=float(input("enter the Temperature in celsius"))
    val=num+273.15
    tup=["from-celsius:",num,"to-kelvin:",val]
    lyst1.append(tup)
    
def celtofah():
    num=float(input("enter the Temperature in celsius"))
    val=float((num * 9/5) + 32)
    tup=["from-celsius:",num,"to-fahrenheit:",val]
    lyst1.append(tup)
        
  
def keltofah():
    num=float(input("enter the Temperature in kelvin"))
    val=float((num - 273.15) * 9/5 + 32)
    tup=["from-kelvin:",num,"to-fahrenheit:",val]
    lyst1.append(tup)
    
def tofrom():
   revlyst=[] 
   for i in range(0,len(lyst1)):
      lyst2=[x for x in lyst1[i]]
      lyst2.reverse()
      j=lyst2[0]
      temp=lyst2[1]
      lyst2[0]=temp
      lyst2[1]=j
      j=lyst2[2]
      temp=lyst2[3]
      lyst2[2]=temp
      lyst2[3]=j
      revlyst.append(tuple(lyst2))
   print(revlyst)   
    
while True:
  print('enter \n1:to convert from celsius to kelvin \n2:to convert from celsius to fahrenheit \n')
  print('3:convert from kelvin to fahrenheit\n4:to display values from -to-values\n5:to display values to-from\n6:exit')
  i=int(input())
  if i==1:
     celtokel()
  elif i==2:
     celtofah()
  elif i==3:
     keltofah()
  elif i==4:
    print(lyst1)
  elif i==5:
    tofrom()
  elif i==6:
    break;
  else:
    print('enter valid command')   
     
        
        