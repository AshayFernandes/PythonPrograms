# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:17:13 2019

@author: Ashay Fernandes
"""
from datetime import date

def AgeConvert(value):
    today=date.today()
    today=str(today)
    value=value.split('-')
    today=today.split('-')
    print(today)
    lyst=[]
    for i in range(0,3):
        lyst.append(int(today[i])-int(value[i]))
    print(lyst)
    totaldays=lyst[0]*365.25
    print(totaldays)
    if(lyst[1]<0):
      totaldays=totaldays-abs(lyst[1])*30.5
    else:
      totaldays=totaldays+lyst[1]*30.5
    if(lyst[2]<0):
        totaldays=totaldays-abs(lyst[2])
    else:
      totaldays=totaldays+lyst[2]  
    print(totaldays)
    age=[]  
    year=totaldays % 365.25
    age.append(totaldays//365.25)
    days=year%30.5
    age.append(year//30.5)
    age.append(int(days))
    
    return age

age=AgeConvert(input("enter your DOB in YEAR-MONTH-DAY format"))
print('your age is{0[0]} years {0[1]} month {0[2]} days'.format(age)) 

    
    
         