#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:26:49 2018

@author: apple
"""

"""
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.

Example
For s1 = "aabcc", s2 = "dbbca"

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

"""
"""
 state: f[i][j]表示s1的前i个字符和s2的前j个字符能否交替组成s3的前i+j个字符
 function: f[i][j] = (f[i-1][j] && (s1[i-1]==s3[i+j-1]) ||
(f[i][j-1] && (s2[j-1]==s3[i+j-1])
 initialize: f[i][0] = (s1[0..i-1] == s3[0..i-1])
f[0][j] = (s2[0..j-1] == s3[0..j-1])
 answer: f[n][m], n = sizeof(s1), m = sizeof(s2)
"""






def isInterleave(s1, s2, s3):
    if s1 is None or s2 is None or s3 is None:
        return False
    if len(s1) + len(s2) != len(s3):
        return False

    interleave = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    interleave[0][0] = True
    for i in range(len(s1)):
        interleave[i + 1][0] = s1[:i + 1] == s3[:i + 1]
    for i in range(len(s2)):
        interleave[0][i + 1] = s2[:i + 1] == s3[:i + 1]

    for i in range(len(s1)):
        for j in range(len(s2)):
            interleave[i + 1][j + 1] = False
            if s1[i] == s3[i + j + 1]:
                interleave[i + 1][j + 1] = interleave[i][j + 1]
            if s2[j] == s3[i + j + 1]:
                interleave[i + 1][j + 1] |= interleave[i + 1][j]
    return interleave[len(s1)][len(s2)]