# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 02:06:42 2019

@author: Ashay Fernandes
"""
dic={'H':'Hydrogen','He':'Helium','O':'oxygen'}


def atomic():
  while True:  
    key=input('enter the element symbolic name')
    value=input('enter the elemenet chemical name')
    dic.update({key:value})
    ch=int(input('enter 0 to exit'))
    if ch==0:
        break
    
  while True:
     key=input('enter the symbollic name of element you need to search ')
     print('the element is {0}'.format(dic.get(key)))
     ch=int(input('enter 0 to exit'))
     if ch==0:
        break 
    
  print('ttal elements in the dictionary is :{0}'.format(len(dic)))  
  
atomic()  