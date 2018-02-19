#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:23:35 2017

@author: apple
"""

"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

"""

def productExceptSelf(nums):
    
    re=list()
    re.append(1)
    temp=1
    for i in range(0, len(nums)-1):
        temp*=nums[i]
        re.append(temp)
    temp=1
    for i in range(len(nums)-2,-1,-1):
        temp*=nums[i+1]
        re[i]*=temp
    return re

print productExceptSelf([1,2,3,4])
#[24, 12, 8, 6]

