#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:34:42 2018

@author: apple
"""

"""
Given a string s, cut s into some substrings such that every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example
Given s = "aab",

Return 1 since the palindrome partitioning ["aa", "b"] could be produced using 1 cut.

"""
"""
解题思路：由于这次不需要穷举出所有符合条件的回文分割，
而是需要找到一个字符串s回文分割的最少分割次数，
分割出来的字符串都是回文字符串。
求次数的问题，不需要dfs，用了也会超时，之前的文章说过，求次数要考虑动态规划（dp）。
对于程序的说明：p[i][j]表示从字符i到j是否为一个回文字符串。
dp[i]表示从第i个字符到最后一个字符，最少的分割次数下，
有多少个回文字符串，即分割次数+1。这道题动态规划的思路比较简单，直接上代码吧。

"""
def minCut(s):

    #dp[i] means from position i to the last how many palindromes there are.
    dp = [0 for i in range(len(s)+1)]
    p = [[False for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s)+1):
        dp[i] = len(s) - i
    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (((j - i) < 2) or p[i+1][j-1]):
                p[i][j] = True
                dp[i] = min(1+dp[j+1], dp[i])
    return dp[0]-1






















