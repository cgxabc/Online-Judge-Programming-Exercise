#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:16:53 2018

@author: apple
"""

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

 Notice

You may assume no duplicate exists in the array.

Have you met this question in a real interview? Yes
Example
Given [4, 5, 6, 7, 0, 1, 2] return 0
"""

def findMin(nums):
    
    if len(nums) == 0 or nums is None:
        return -1
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (start + end) / 2
        if nums[mid] > nums[start]:
            if nums[start] > nums[end]:
                start = mid
            else:
                end = mid
        else:
            end = mid
                
    if nums[start] < nums[end]:
        return nums[start]
    else:
        return nums[end]
    