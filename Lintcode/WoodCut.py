#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:22:13 2018

@author: apple
"""

"""
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

 Notice

You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.

Example
For L=[232, 124, 456], k=7, return 114.
"""
def woodCut(L, k):
    if sum(L) < k:
        return 0
            
    maxLen = max(L)
    start, end = 1, maxLen
    while start + 1 < end:
        mid = (start + end) / 2
        pieces = sum([l / mid for l in L])
        if pieces >= k:
            start = mid
        else:
            end = mid
        
    if sum([l / end for l in L]) >= k:
        return end
    return start