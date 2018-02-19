#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:25:55 2017

@author: apple
"""

"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

def divide(dividend, divisor):
    if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
        if abs(dividend)<abs(divisor):
            return 0
    sum=0
    count=0
    res=0
    a=abs(dividend)
    b=abs(divisor)
    while a>=b:
        sum=b
        count=1
        while sum+sum<=a:
            sum+=sum
            count+=count
        a-=sum
        res+=count
    if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
        res=0-res
    if res>2147483647:
        return 2147483647
    else:
        return res