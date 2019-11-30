# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 00:36:38 2019

@author: Ashay Fernandes
"""


atmdi={ "H":"Hydrogen","O":"Oxygen","C":"carbon","Na":"Sodium","He":"Helium"
        
       }
def AtomicDictionary():
     
   while True:
     ki=input("enter the key :")
     val= input("enter the value:")
     atmdi.update({ki:val})
     che=input("enter 0 to finish entering the elements or press enter to continue")
     if che=='0':
       break 
   print('The total number of elements in the Dictionary are:',len(atmdi))
   
   while True:
       key_value=input("enter the key for which you require value")
       print(atmdi.get(key_value))
       che=input("enter 0 to finish  or press enter to continue")
       if che=='0':
         break
     
AtomicDictionary()      