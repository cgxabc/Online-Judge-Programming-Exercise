#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:58:33 2017

@author: apple
"""

"""
Find the contiguous subarray within an array 
(containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
def maxSubArray(nums):
    for i in xrange(1,len(nums)):
        nums[i]=max(nums[i],nums[i]+nums[i-1])
    return max(nums)

def maxSubArray2(nums):
    cur=nums[0]
    maxSum=nums[0]
    for num in nums[1:]:
        cur=max(num, cur+num)
        maxSum=max(cur,maxSum)
        
    return maxSum
        