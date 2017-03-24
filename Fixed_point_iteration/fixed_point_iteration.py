#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:40:55 2017

@author: user
"""

def func_1(x):
    return (1 + (1. / x))
        
def func_2(x):
    return ((x ** 3 + 2.) / 7)
      

part_no = int(input("Enter Part Number  1 or 2: "))
var = float(input("Enter value: "))

if(part_no == 1):
    y = func_1(var)
    while(abs(y - var) > 0.0005):
        var = y
        y = func_1(var)
    print (var)
if(part_no == 2):
    y1 = func_2(var)
    if(var < (47 ** (1./3))):
        while(abs(y1 - var) > 0.0005):
            var = y1
            y1 = func_1(var)
        print (var)
    else:
        print("Non converging")
