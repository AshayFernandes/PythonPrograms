# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 01:45:16 2019

@author: Ashay Fernandes
"""

class student:
    def __init__(self):
        self.name=0
        self.age=0
        self.marks=[]
        
    def accept(self):
        self.name=input('Enter student name')
        self.age=int(input('Enter student age'))
        print('enter marks obtained in three subjects')
        for i in range(3):
         self.marks.append(int(input()))
         
    def display(self):
       print('student name:{0}\nstudent age:{1}\nmarks in three subjects:{2}'.format(self.name,self.age,self.marks)) 
        
 
    
s1=student()
s2=student()

s1.accept()
s2.accept()

s1.display()
s2.display()       
        