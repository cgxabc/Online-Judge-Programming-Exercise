#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:32:38 2017

@author: apple
"""

def firstUniqChar(s):
    letters={}
    for c in s:
        if c in letters:
            letters[c]+=1
        else:
            letters[c]=1
    for i in range(len(s)):
        if letters[s[i]]==1:
            return i
    return -1
    
    
    
    
print firstUniqChar("leetcode")
    
    
