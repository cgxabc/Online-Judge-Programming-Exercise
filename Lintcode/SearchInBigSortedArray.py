#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:16:18 2018

@author: apple
"""
"""
Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example

Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

"""
def searchBigSortedArray(A, reader, target):
    index = 0
    while reader.get(index) < target:
        index = index*2 + 1
    start, end = 0, index
    while reader.get(index) < target:
        index = index*2 + 1
        
    start, end = 0, index
    while start + 1 < end:
        mid = (start + end) / 2
        if reader.get(mid) >= target:
            end = mid
        else:
            start = mid
    if reader.get(start) == target:
        return start
    if reader.get(end) == target:
        return end
    return -1
    
    
