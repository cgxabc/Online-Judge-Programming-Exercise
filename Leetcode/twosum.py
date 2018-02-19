#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:04:35 2017

@author: apple
"""

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the SAME ELEMENT twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum(nums, target):
    idxDict={}
    for idx, num in enumerate(nums):
        idxDict[num]=idx
    
    for idx, num in enumerate(nums):
        if target-num in idxDict.keys() and idxDict[target-num]<>idx:
            return [idxDict[target-num], idx]
        
print twoSum([3,2,4],6)
##[2, 1]