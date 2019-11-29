# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 01:24:14 2019

@author: Ashay Fernandes
"""
#classes in python
class Person:
  def __init__(self,name,age): #constructor of the class Person
    self.name=name;
    self.age=age;
   
p1=Person("Suppandi",14)
p2=Person("Ramu",12)

print("\n Name of Person #1 is",p1.name)
print("\n Age of person #1 is",p1.age)

print("\n Name of Person #2 is",p2.name)
print("\n Age of person #2 is",p2.age)

p2.age=10 #attributes of object is modified

print("\nModified age of Person #2 is",p2.age)
      
#Using del functions to delete the attributes of an object and the object itself

class Person:
  def __init__(self,name,age):
    self.name=name;
    self.age=age;

p1=Person("Suppandi",14)

print("\nName of Person is",p1.name)
print("\nAge of Person is",p1.age)

print("\n**Printing after deleting  age attribute for p1**")
del p1.age #deleting age attribute for p1 object
print("\n Name of Person is",p1.name)
#print("\nAge of Person is",p1.age) #Error is: AttributeError:'Person' object has no attribute 'age'


print("\n**Printing after deleting p1**")
del p1
#print("\nName of Person is",p1.name)
#NameError: name 'p1' is not defined
      
