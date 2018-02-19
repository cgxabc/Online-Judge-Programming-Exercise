#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:09:11 2017

@author: apple
"""

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

def strStr(haystack, needle):
    for i in xrange(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1

def strStr2(haystack, needle):
    return haystack.find(needle)