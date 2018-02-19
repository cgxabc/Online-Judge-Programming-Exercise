#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:44:56 2018

@author: apple
"""

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
def lengthOfLongestSubstring(s):
    ans, start, end = 0, 0, 0
    countDict = {}
    for c in s:
        end += 1
        countDict[c] = countDict.get(c, 0) + 1
        while countDict[c] > 1:
            countDict[s[start]] -= 1
            start += 1
        ans = max(ans, end - start)
    return ans
            
 
def lengthOfLongestSubstring2(s): 
    a={}
    count=0
    first=-1
    for i in range(len(s)):
        if s[i] in a and a[s[i]]>first:
            first=a[s[i]]
        a[s[i]]=i
        count=max(count,(i-first))
    return count


