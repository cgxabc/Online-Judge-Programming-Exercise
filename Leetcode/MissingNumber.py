#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 01:26:35 2017

@author: apple
"""

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

"""

def missingNumber1(nums):
    
    res=len(nums)
    for i in range(len(nums)):
        res^=(i^nums[i])
    return res



def missingNumber2(nums):
    temp_sum=len(nums)*(len(nums)+1)/2
    t_sum=sum(nums)
    return temp_sum-t_sum
    
      
print missingNumber1([0])
print missingNumber2([0,2])