#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:46:05 2017

@author: apple
"""

"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
def isPalindrome(x):
    if x<0:
        return False
    temp=x
    reverse=0
    while temp:
        reverse=reverse*10+temp%10
        temp=temp/10
    return reverse==x
        