#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:28:33 2018

@author: apple
"""

"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

def wordBreak(s, dict):
    dp=[False for i in range(len(s)+1)]
    dp[0]=True
    for i in range(1, len(s)+1):
        for k in range(i):
            if dp[k] and s[k:i] in wordDict:
                dp[i]=True
    return dp[len(s)]
    
def wordBreak2(s, dict):
    if len(dict) == 0:
        return len(s) == 0
            
    n = len(s)
    f = [False] * (n + 1)
    f[0] = True
        
    maxLength = max([len(w) for w in dict])
    for i in xrange(1, n + 1):
        for j in range(1, min(i, maxLength) + 1):
            if not f[i - j]:
                continue
            if s[i - j:i] in dict:
                f[i] = True
                break
        
    return f[n]
    
    
    