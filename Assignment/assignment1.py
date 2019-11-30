# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:56:53 2019

@author: Ashay Fernandes
"""

"""<q> Create a list and do the  following manipulation
1> Find the length of the list
2>Create a new list as an element of an existing list
3>use the slice Operator
4>Replace the second element of the list with  a fruit name 
5>concatenate two list
6>Find atleast two ways to copy and clone a list
7>find out atleast one way to split a list into evenly sized chunks """

#<q>list of seven wonders of the  Ancient World
lst1=["The Great Pyramid of Giza","Hanging Gardens of Babylon","Colossus of Rhodes","Temple of Artemis","light house of Alexandria","Statue of Zeus at Olympia","Mausoleum at Halicarnassus"]

 #1>
print('Length of the List is :',len(lst1))

#2>
lst2=[]
for i in range(0,4):
    lst2.append(lst1[i])
print(lst2)    

#3>
lst3=lst1[4:]
print(lst3)

#4>
lst1[1]='PEACH'

#5>seven wonders of Modern World
lst4=['Taj Mahal','Christ The Redeemer','Petra','The Great Wall Of China','The Colosseum Of Rome','Machu Picchu','Chichen Itza' ]
lst5=lst1 + lst4
print(lst5)

#6>method 1
clst1=lst1[:]

 #method2
clst2=list(lst1) 

#method3
clst3=lst4.copy()

#method5
import copy
clst4=copy.copy(lst1)

#7>
def chuck(listx,chunksize):
       finalist=[]
       for i in range(0,len(lst1),chunksize):
         finalist.append(lst1[i:i+chunksize])
       return finalist
   
lst7=[]  
lst7=chuck(lst1,2)  

"""<q2>write a Python Program to create a tuple with number and print one item"""
tpl_number=(9,4,8,2,6,9,6,0,1,6)
print(tpl_number[5])

"""<q3>convert the tuple to list"""
tlst=list(tpl_number)
