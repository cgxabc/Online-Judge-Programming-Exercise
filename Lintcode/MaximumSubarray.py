#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:35:49 2018

@author: apple
"""

"""
Given an array of integers, find a contiguous subarray which has the largest sum.

 Notice

The subarray should contain at least one number.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

"""
def maxSubArray(nums):
    ThisSum = 0
    MaxSum = -10000
        
    for i in range(len(nums)):
        if ThisSum < 0:
            ThisSum = 0
        ThisSum = ThisSum + nums[ i ]
        MaxSum = max( ThisSum, MaxSum )

    return MaxSum