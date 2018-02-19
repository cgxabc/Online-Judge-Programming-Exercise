#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:23:40 2018

@author: apple
"""

"""
Binary search is a famous question in algorithm.

For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

"""
def binarySearch(nums, target):
    if len(nums) == 0:
        return -1
    start, end = 0, len(nums)-1
    while start + 1 < end:
        mid = (start + end) / 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid
            
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1
            


