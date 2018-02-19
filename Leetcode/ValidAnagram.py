#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:29:14 2017

@author: apple
"""

def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    letters_s={}
    letters_t={}
    for i in s:
        letters_s[i]=letters_s.get(i,0)+1
    for n in t:
        letters_t[n]=letters_t.get(n,0)+1
    return letters_s==letters_t


def isAnagram2(s,t):
    return sorted(s) == sorted(t)

print isAnagram("rat","car")
print isAnagram2("anagram","nagaram")