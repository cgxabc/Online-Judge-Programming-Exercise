#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:11:43 2018

@author: apple
"""

"""
Given a string and an offset, rotate string by offset. (rotate from left to right)

Example
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
"""

def rotateString(str, offset):
    if str is None or len(str)==0:
            return str
        
    offset%=len(str)
    before=str[ :len(str)-offset]
    after=str[len(str)-offset: ]
    temp=before[::-1]+after[::-1]
    temp=temp[::-1]
    for i in xrange(len(temp)):
           str[i]=temp[i]
           

def rotateString2(str, offset):
    if len(str)>0:
        offset%=len(str)
        
    temp=(str+str)[len(str)-offset: 2*len(str)-offset]
    for i in xrange(len(temp)):
        str[i]=temp[i]









#print rotateString('abcdefg',3)

#efgabcd

#s='abc'
#print s+s
#abcabc
            
