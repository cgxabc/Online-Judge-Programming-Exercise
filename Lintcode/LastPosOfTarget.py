#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:50:42 2018

@author: apple
"""

def lastPosition(nums, target):
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) / 2
        if nums[mid] == target:
            start = mid
        elif nums[mid] < target:
            start = mid
        else:
            end = mid
            
    if nums[end] == target:
        return end
    if nums[start] == target:
        return start
    return -1