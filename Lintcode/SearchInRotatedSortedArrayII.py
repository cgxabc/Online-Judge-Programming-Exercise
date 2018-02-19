#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:40:45 2018

@author: apple
"""

"""
Follow up for Search in Rotated Sorted Array:

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

Have you met this question in a real interview? Yes
Example
Given [1, 1, 0, 1, 1, 1] and target = 0, return true.
Given [1, 1, 1, 1, 1, 1] and target = 0, return false.

"""
def search(A, target):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = start + (end - start) / 2
        if A[mid] == target:
            return True
        if A[start] == A[mid] == A[end]:
            start += 1
            end -= 1
        elif A[start] <= A[mid]:
            if A[start] <= target < A[mid]:
                end = mid -1
            else:
                start = mid + 1
        else:
            if A[mid] < target < A[end]:
                start = mid + 1
            else:
                end = mid - 1
    return False
            
    