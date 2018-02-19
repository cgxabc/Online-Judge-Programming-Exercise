#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:08:52 2018

@author: apple
"""

"""
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Have you met this question in a real interview? Yes
Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
Example
If source = "source" and target = "target", return -1.

If source = "abcdabcdefg" and target = "bcd", return 1.
"""
def strStr1(source, target):
   # write your code here
    if source is None or target is None:
        return -1
    return source.find(target)


def strStr1(source, target):
   if source is None or target is None:
      return -1
   for i in range(0,len(source)-len(target)+1):
      if source[i:i+len(target)]==target:
         return i
   return -1