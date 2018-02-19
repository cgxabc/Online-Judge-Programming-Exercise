#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:36:40 2017

@author: apple
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

def findMin(nums):
    low=0
    high=len(nums)-1
    while low<high:
        mid=(low+high)/2
        if nums[mid]<=nums[high]:
            high=mid
        else:
            low=mid+1
    return nums[low]


def findMin2(nums): 
    return min(num)