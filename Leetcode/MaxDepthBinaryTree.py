#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:07:04 2017

@author: apple
"""

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""
def singleNumber(nums):
    
    for i in nums:
        a=nums[0]
        for i in range(1, len(nums)):
            a=a^nums[i]
        return a
       # if i not in temp:
           # return i
        
print singleNumber([2,4,4,5,2,5,6])
