#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:37:04 2017

@author: apple
"""
"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""


def findMin(nums):
    
    low=0
    high=len(nums)-1
    while low<high:
        mid=(low+high)/2
        if nums[mid]<nums[high]:
            high=mid
        elif nums[mid]>nums[high]:
            low=mid+1
        else:
            high-=1
            
    return nums[low]

def findMin(nums):
    return min(nums)