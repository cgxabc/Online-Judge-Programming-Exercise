#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 00:52:32 2017

@author: apple
"""

"""
Write a function that takes an unsigned integer 
and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' 
has binary representation 00000000000000000000000000001011, 
so the function should return 3.
"""
#按照定义，将输入的数表示成二进制的字符串，数一下有多少个1即可。
def hammingWeight(n):
    return bin(n).count('1')

#通过移位操作，一位一位的判定是否是数字1。
def hammingWeight2(n):
    count=0
    while n:
        count+=n&1
        n>>1
    return count