#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:32:10 2017

@author: apple
"""

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""

def isValid(s):
    stack=[]
    match_dict={"(":")", "{":"}","[":"]"}
    for item in s:
        if item in match_dict:
            stack.append(item)
        elif len(stack)==0 or match_dict[stack.pop()]!=item:
            return False
    return len(stack)==0
            