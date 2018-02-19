#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:12:26 2018

@author: apple
"""
"""
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.


Clarification
What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm
Example
For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.

For "ABCD" and "EACB", the LCS is "AC", return 2.
"""
def longestCommonSubsequence(A, B):
    n, m = len(A), len(B)
    f = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            f[i][j] = max(f[i-1][j], f[i][j-1])
            if A[i-1] == B[j-1]:  #the ith of A compares with the jth of B
                f[i][j] = f[i-1][j-1] + 1
    return f[n][m]