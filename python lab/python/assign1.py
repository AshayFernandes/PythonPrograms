# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:27:51 2019

@author: Ashay Fernandes
"""
"""
<q> Write a python progran to do the following:
   a) Read a list of elemets. Create a new list having all the elements minus duplicate use functions.use 
      one line comprehensions to create a new list of even numbers . create another list reversing the elements.
    """  
lyst1=[]    
for i in range(0,5):
       lyst1.append(int(input("enter the list element(numbers)\n")));
lyst2=[]      
def deldup(lyst):
   for i in lyst1:
      if i not in lyst2:
         lyst2.append(i) 
         
deldup(lyst1) 
print(lyst2)
        
     
#using list comprehension to generate a list of even numbers

lyst3=[x for x in lyst1 if x%2==0]
print(lyst3)    

#reversing the list 
lyst4=[x for x in lyst1]
lyst4.reverse()
print(lyst4)

"""
 b)write a python program to count the frequency of words in a given file
 """
fhand=open('text.txt')
x=fhand.read()
lyst5=[]
lis=x.split()
dic={}
for i in lis :
   dic[i]=dic.get(i,0)+1
for key,values in dic.items():   
    print(key,values)

   