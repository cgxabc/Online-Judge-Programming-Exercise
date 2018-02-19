#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:40:40 2017

@author: apple
"""
"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
"""
"""
我们在区间[1, n]中搜索，首先求出中点mid，
然后遍历整个数组，统计所有小于等于mid的数的个数，
如果个数小于mid，则说明重复值在[mid+1, n]之间，
反之，重复值应在[1, mid-1]之间，然后依次类推，直到搜索完成，
此时的low就是我们要求的重复值。
"""

def findDuplicate(nums):
    low=0
    high=len(nums)-1
    while (low<high):
        mid=low+(high-low)/2
        count=0
        for i in nums:
            if i<=mid:
                count+=1
        if count<=mid:
            low=mid+1
        else:
            high=mid-1
    return low

print findDuplicate([1,2,2,3])
        
    