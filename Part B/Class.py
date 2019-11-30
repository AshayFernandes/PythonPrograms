# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:29:19 2019

@author: Ashay Fernandes
"""

def secondval(x):
     return x[1]
class Reverse:
    
    def __init__(self,value):
        self.value=value
        self.count=0
        self.string=[]
        
    def rev(self):
        lyst1=self.value.split()
        lyst1.reverse()
        strin=' '
        self.string=strin.join(lyst1)
        
        for x in self.string:
            if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
                self.count=self.count+1
                
    def display(self,ob1,ob2):
        lyst2=[[self.string,self.count],[ob1.string,ob1.count],[ob2.string,ob2.count]]
        lyst2.sort(key=secondval,reverse=True)   
        for x,y in lyst2:
            print(x)
            
string1=input('first')
string2=input('second')
string3=input('third')

s1=Reverse(string1)
s2=Reverse(string2)
s3=Reverse(string3)
s1.rev()
s2.rev()
s3.rev()
s1.display(s2,s3)            
            