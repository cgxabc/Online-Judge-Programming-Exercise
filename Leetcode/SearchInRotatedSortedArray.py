#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:31:09 2017

@author: apple
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

def search(nums, target):
    
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)/2 
        if target==nums[mid]:
            return mid
        if nums[mid]>=nums[left]:   #the left side is sorted
            if target<nums[mid] and target>=nums[left]:
                right=mid-1
            else:
                left=mid+1
        elif nums[mid]<nums[right]:
            if target>nums[mid] and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
    return -1

print search([4,5,6,7,0,1,2],1)
#5