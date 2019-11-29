# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:06:03 2019

@author: Ashay Fernandes
"""

def HourMinute(value):
    hour=value//60
    minute=value%60
    
    print('{0}:{1}'.format(hour,minute))
    
HourMinute(int(input('Enter the number of minutes')))   
