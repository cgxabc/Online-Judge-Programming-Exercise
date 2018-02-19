#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:39:34 2018

@author: apple
"""

"""
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 1 or 2.

For target = 5, return 4 or 5.

For target = 6, return -1.
"""
def findPosition(nums, target):
    
    if len(nums) == 0 or nums is None:
            return -1
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (start + end)/2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid
        elif target > nums[mid]:
            start = mid
        
    if target == nums[start]:
        return start
    if target == nums[end]:
        return end
    return -1   