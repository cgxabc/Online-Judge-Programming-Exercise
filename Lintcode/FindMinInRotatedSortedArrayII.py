#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:49:32 2018

@author: apple
"""

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

 Notice

The array may contain duplicates.

Example
Given [4,4,5,6,7,0,1,2] return 0.

"""
def findMin(nums):
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start + end)/ 2
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[end]:
            end = mid
        else:
            end = end - 1
    return nums[start]