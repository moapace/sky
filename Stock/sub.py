# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:46:25 2018

@author: MorrisCheng
"""
from __future__ import print_function
import requests
import sys



def fibonacci(n):
    if n < 2:
        return n
    else:
        val = fibonacci(n-1)+fibonacci(n-2)
        
    print("f(",n,')=',val,end=' ')
    return val

def showpath():
    print ("List default module path:")
    for i in sys.path:
       print(i)
       
print ("Test fibonacci n=5")
print ("series:")
print (fibonacci(4))

r = requests.get('http://tw.yahoo.com')
print ("check connection:", r.status_code)
print ("coding:",r.encoding)
showpath()
