#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:55:53 2017

@author: apple
"""
"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""

def maximumGap(nums):
    if len(nums)<2:
        return 0
    
    nums.sort()
    pre=nums[0]
    max_gap=float("-inf")
    
    for i in nums:
        max_gap=max(max_gap,i-pre)
        pre=i
    return max_gap