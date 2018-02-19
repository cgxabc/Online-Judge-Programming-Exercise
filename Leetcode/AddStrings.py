#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:11:46 2018

@author: apple
"""

"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
def addString(num1, num2):
    return str(int(num1)+int(num2))

def addString2(num1, num2):
    result=[]
    flag=0
    idx1=len(num1)
    idx2=len(num2)
    while idx1 or idx2 or flag:
        sum_digit=flag
        if idx1:
            idx1-=1
            sum_digit+=int(num1[idx1])
        if idx2:
            idx2-=1
            sum_digit+=int(num2[idx2])
        if sum_digit>9:
            flag=1
        else:
            flag=0
        result.append(str(sum_digit%10))
    return ''.join(result[::-1])

print addString2('43','567')  #610











    