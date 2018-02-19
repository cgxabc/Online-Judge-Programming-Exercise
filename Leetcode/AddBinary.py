#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:25:25 2017

@author: apple
"""

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

def addBinary(a,b):
    res = ''
    i, j, plus = len(a)-1, len(b)-1, 0
    while i>=0 or j>=0 or plus==1:
       plus += int(a[i]) if i>= 0 else 0
       plus += int(b[j]) if j>= 0 else 0
       res = str(plus % 2) + res
       i, j, plus = i-1, j-1, plus/2
    return res


def addBinary2(a,b):
    return bin(int(a, 2) + int(b, 2))[2:]

