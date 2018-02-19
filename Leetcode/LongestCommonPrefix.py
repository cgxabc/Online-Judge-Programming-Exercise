#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:54:02 2017

@author: apple
"""

"""
Write a function to find the longest common prefix string 
amongst an array of strings.
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    for i in xrange(len(strs[0])):
        for string in strs[1:]:
            if i>=len(string) or string[i]!=strs[0][i]:
                return strs[0][:i]
    return strs[0]
            