# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:07:59 2019

@author: Ashay Fernandes
"""

lyst=["ashay","clinton","fernandes",2,3]

def chunks(lyst,chunksize):
    newlyst=[]
    for i in range(0,len(lyst),chunksize):
        newlyst.append(lyst[i:i+chunksize])
    return newlyst
    
ne=chunks(lyst,2)






    