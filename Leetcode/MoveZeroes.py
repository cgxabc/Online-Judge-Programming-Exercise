#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:56:21 2017

@author: apple
"""

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

def moveZeroes(nums):
    k=0
    for i in nums:
        if i!=0:
            nums[k]=i
            k+=1
    nums[k:]=[0]*(len(nums)-k)   ##set the rest of the list to zeros
    return nums
     
     
print moveZeroes([0,0,1]) 
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     