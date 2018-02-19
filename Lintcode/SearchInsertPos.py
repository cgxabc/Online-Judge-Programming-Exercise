#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:14:47 2018

@author: apple
"""

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Have you met this question in a real interview? Yes
Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0

"""
def searchInsert(A, target):
    if len(A)==0:
        return 0
    start, end = 0, len(A)-1
    while start + 1 < end:
         mid = start + (end - start) / 2
         if A[mid] >= target:
            end = mid
         else:
            start = mid
                
    if A[start] >= target:
        return start
    if A[end] >= target:
        return end
            
    return len(A)