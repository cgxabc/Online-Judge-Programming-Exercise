#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:18:30 2018

@author: apple
"""

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

"""
def search(A, target):
    if A is None or len(A)==0:
        return -1
    start = 0
    end = len(A) - 1
    while start + 1 < end:
        mid = start + (end - start)/2
        if A[mid] == target:
            return mid
        if A[start] < A[mid]:
            if A[start] <= target and target <= A[mid]:
                end = mid
            else:
                start = mid
        else:
            if A[mid] <= target and target <= A[end]:
                start = mid
            else:
                end = mid
     if A[start] == target:
         return start
     if A[end] == target:
         return end
     return -1
    

    