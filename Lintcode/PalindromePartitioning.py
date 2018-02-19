#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:33:30 2018

@author: apple
"""

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]

"""
def partition(self, s):
        # write your code here
        if not s:
            return [[]]
        result = []
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                for r in self.partition(s[i+1:]):
                    result.append([s[:i+1]]+r)
        return result
        
def isPalindrome(self, s):
     return s==s[::-1]

