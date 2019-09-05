# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:24:13 2019

@author: Ashay Fernandes
"""

""" <q> <1> Create a python class called 'Student' having 'name','age, as attribute along with a
    list having the marks obtained for three subjects.
    <2> create a constructor to initialize two objects of this class
    <3> create a  member function called 'display' printing the details of the
       specific object.
    <4>Ask user to enter the values for an object through an 'accept' member functions
    <5>Display these details
""" 
class Student:
    
    def __init__(self):
        self.lst1=[]
                  
    def accept(self):
        self.name=input("Enter Student name :")
        self.age=input("Enter Student age :")
        for i in range(0,3):
           self.lst1.append(input("enter marks of Student in three Subjects:"))            
        
    def disp(self):
        print('Name Of Student :',self.name)
        print(' Age Of Student :',self.age)
        print('Marks of the Student in subjectis:',self.lst1)
  
Student1=Student()
Student2=Student()
# 
Student1.accept() 
Student2.accept()

Student1.disp()
Student2.disp()

""" <q2> Create a dictionary to hold student Details with register numbers as the key
    . print those student details whose register numbers are even
"""
studi={"1MS17IS000":["James",19,"O+"],"1MS17IS001":["Jimmy",20,"AB-"],"1MS17IS002":["John",21,"O-"],
       "1MS17IS003":["Ellen",18,"AB+"],"1MS17IS004":["Coco",25,"O+"]
          
          } 
for i in studi:
    val=int((i[7:10]))
    if val%2 == 0.0:
        print(studi.get(i)) 
  
"""<q3> 1> Create a dictionary that contains the atomic element Symbol and the name
        2> Add a unique and duplicate element into this dictionary by interacting with the user.
          Observe the output and justify
        3> Display he numbers of atomic elements in this dictionary
        4> Ask the user to enter an element to search in the dictionary. Display 
           appropriate results
         Rewrite this program so that these operations are inside a function called 'AtomicDictionary'.
         Create another python file called "Atomic.py" and execute this function in it
"""
 
atmdi={ "H":"Hydrogen","O":"Oxygen","C":"carbon","Na":"Sodium","He":"Helium"
        
       }

while True:
    ki=input("enter the key :")
    val= input("enter the value:")
    atmdi.update({ki:val})
    che=input("enter 0 to finish entering the elements or press enter to continue")
    if che=='0':
      break      
   
print('The total number of elements in the Dictionary are:',len(atmdi))

key_value=input("enter the key for which you require value")
print(atmdi.get(key_value))
        
    
    
    
    
    
    
      
    
    
    