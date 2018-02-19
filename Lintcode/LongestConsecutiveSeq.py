#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 23:47:49 2018

@author: apple
"""

"""
Given an unsorted array of integers, 
find the length of the longest consecutive elements sequence.


Clarification
Your algorithm should run in O(n) complexity.

Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. 
Return its length: 4.

"""
def longestConsecutive(num):
     dict = {x: False for x in num} # False means not visited
     maxLen = 1
     for i in dict:
         if dict[i] == False:
             curr = i+1
             lenright = 0
             while curr in dict:
                lenright += 1
                dict[curr] = True
                curr += 1
                  
              curr = i-1
              lenleft = 0
              while curr in dict:
                 lenleft += 1
                 dict[curr] = True
                 curr -= 1
              maxLen = max(maxLen, lenleft+1+lenright)
    return maxLen