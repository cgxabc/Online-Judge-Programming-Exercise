#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:22:47 2018

@author: apple
"""

"""
Given an array S of n integers, 
find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

def threeSumClosest(nums, target):
    nums.sort()
    mindiff=100000
    res=0
    for i in range(len(nums)):
        left+=i
        right=len(nums)-1
        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            diff=abs(sum-target)
            if diff<mindiff:
                mindiff=diff
                res=sum
            if sum==target:
                return sum
            elif sum<target:
                left+=1
            else:
                right-=1
    return res
    
    
