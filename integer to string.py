# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:00:00 2018

@author: lenovo
"""

def intToStr(i):
    digits = '0123456789'
    if i == 0 :
        return '0'
    result = ''
    while i > 0 :
        result = digits[i % 10] + result
        i = i//10
    return result
    

# There is another simple way for solving the problem

def inToStr(i):
    answer = str(i)
    return answer