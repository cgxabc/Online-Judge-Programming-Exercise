#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:48:21 2017

@author: apple
"""

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


#pattern='abbacc'
#str1='dog cat cat dog tiger tiger'
#print map(pattern.find, pattern)
#words=str1.split(' ')
#print map(words.index, words)
#[0, 1, 1, 0, 4, 4]
#[0, 1, 1, 0, 4, 4]
def wordPattern(pattern, str):
    words=str.split(' ')
    if len(words)!=len(pattern):
        return False
    return map(pattern.find, pattern)==map(words.index, words)
    
    
def wordPattern2(pattern, str):
    words=str.split(' ')
    if len(words)!=len(pattern):
        return False
    return len(set(pattern))==len(set(words))==len(set(zip(pattern, words)))

def wordPattern3(pattern, str):
    words=str.split(' ')
    if len(words)!=len(pattern):
        return False
    hashmap={}
    mapval={}
    for i in xrange(len(pattern)):
        if pattern[i] in hashmap:
            if hashmap[pattern[i]]!=words[i]:
                return False
        else:
            if words[i] in mapval:
                return False
            hashmap[pattern[i]]=words[i]
            mapval[words[i]]=True
    return True
            
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    