#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:26:47 2018

@author: apple
"""

"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example
Given S = "rabbbit", T = "rabbit", return 3.

"""
"""
 state: f[i][j] 表示 S的前i个字符中选取T的前j个字符，有多少种方案
• function: f[i][j] = f[i - 1][j] + f[i - 1][j - 1] // S[i-1] == T[j-1]
• = f[i - 1][j] // S[i-1] != T[j-1]
• initialize: f[i][0] = 1, f[0][j] = 0 (j > 0)
• answer: f[n][m] (n = sizeof(S), m = sizeof(T))

"""
def numDistinct(S, T):
    dp = [[0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]
    for i in range(len(S) + 1):
       	dp[i][0] = 1
    for i in xrange(len(S)):
        for j in xrange(len(T)):
            if S[i] == T[j]:
                dp[i+1][j+1] = dp[i][j+1] + dp[i][j]
            else:
                dp[i+1][j+1] = dp[i][j + 1]
    return dp[len(S)][len(T)]
    