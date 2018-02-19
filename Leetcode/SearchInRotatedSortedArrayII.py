#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:15:13 2017

@author: apple
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

"""

def search(nums, target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)/2 
        if target==nums[mid]:
            return True
        if nums[left]==nums[mid] and nums[mid]==nums[right]:
            left+=1
            right-=1
        elif nums[mid]>=nums[left]:   #the left side is sorted
            if target<nums[mid] and target>=nums[left]:
                right=mid-1
            else:
                left=mid+1
        else:
            if target>nums[mid] and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
    return False