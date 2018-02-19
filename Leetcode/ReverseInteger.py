#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:29:15 2017

@author: apple
"""
"""
1.python里面int最大数值0x7FFFFFFF，在考虑溢出的时候需要和这个值进行比较。

2.取模运算可以得到数字的最后一位，/运算会得到移走最后一个数字之外的数字，以此循环




"""
def reverse(x):
    res=0
    sign=-1 if x<0 else 1
    x=x*sign
    while (x):
        res=res*10+x%10
        x=x/10
    if res>0x7FFFFFFF:
        return 0
    return res*sign

print reverse(123)
print reverse(-123)