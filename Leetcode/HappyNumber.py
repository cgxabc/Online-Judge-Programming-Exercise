#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:57:20 2017

@author: apple
"""

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, 
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
def calculate(n):
    sum_digits=0
    while n>0:
        sum_digits+=(n%10)*(n%10)
        n/=10
    return sum_digits

#print calculate(19)

#82=1^2+9^2


def isHappy(n):
    history=[]
    sum_digits=0
    while True:
        if n==1:
            return True
        while n>0:
            sum_digits+=(n%10)*(n%10)
            n/=10
        if sum_digits in history:
            return False
        else:
            history.append(sum_digits)
            n=sum_digits
            sum_digits=0
    
print isHappy(19)