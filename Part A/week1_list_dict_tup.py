# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 01:09:10 2019

@author: Ashay Fernandes
"""

#DICTONARY
mydictionary= {
"name": "Archie",
"identity": "Student",
"age": 17
}
print(mydictionary)

key = mydictionary["name"]
value = mydictionary.get("name")
print("Key is",key)
print("Value is",value)


#DICTIONARY AND LIST
students = {'1MS16IS100':'Asha', '1MS16IS101':'ashok','1MS16IS102':'Rekha','1MS16IS103':'Suma'}
list1 = ["value1","value2","value3","value4"]
list2=["a","b","c","d"]


#printing student names
j=0;
for i in students:
 print("Key is ",i, "Value is ",students[i])
 list1[j]=students[i]
 list2[j]=i
 j=j+1

print(list1)
print(list2)
print(students.keys())
print(students.values())
print(students.items())


#IF-ELSE
x=-3
if x>0.0:
  print("Positive")
elif x<0.0:
  print("Negative")
  x=-1.0*x
else :
  print("Zero")

