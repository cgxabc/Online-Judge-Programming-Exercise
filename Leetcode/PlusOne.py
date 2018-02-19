#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:14:21 2017

@author: apple
"""

"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

def plusOne(digits):
    digits=[str(x) for x in digits]
    num=int(''.join(digits))+1
    return [int(x) for x in str(num)]

def plusOne2(digits):
    flag=1
    for i in range(len(digits)-1,-1,-1):
        if digits[i]+flag==10:
            digits[i]=0
            flag=1
        else:
            digits[i]=digits[i]+flag
            flag=0
    if flag==1:
        digits.insert(0,1)
    return digits

print plusOne2([1,4,5,9])
           
#[1, 4, 6, 0]