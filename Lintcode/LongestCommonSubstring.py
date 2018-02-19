#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:33:31 2018

@author: apple
"""

"""
Given two strings, find the longest common substring.

Return the length of it.

 Notice

The characters in substring should occur continuously in original string. This is different with subsequence.

Example
Given A = "ABCD", B = "CBCE", return 2.

"""
def longestCommonSubstring(A, B):
    # write your code here
    #state: f[i][j] is the length of the longest lcs
    # ended with A[i - 1] & B[j - 1] in A[0..i-1] & B[0..j-1]
    n=len(A)
    m=len(B)
    f= [ [0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1]!=B[j-1]:
                f[i][j]=0
            else:
                f[i][j] = f[i-1][j-1]+1
    max_length = 0 
    for i in range(1, n+1):
        for j in range(1, m+1):
            max_length = max(max_length, f[i][j])
    return max_length


def longestCommonSubstring2(A, B):
    ans = 0
    for i in xrange(len(A)):
        for j in xrange(len(B)):
            l = 0
            while i + l < len(A) and j + l < len(B) and A[i + l] == B[j + l]:
               l += 1
            ans=max(ans, l)
    return ans
        
















    