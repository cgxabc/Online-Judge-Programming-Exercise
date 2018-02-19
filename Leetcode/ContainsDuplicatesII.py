#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:33:54 2017

@author: apple
"""

"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""

def containsNearbyDuplicate(nums, k):
    num_map = {}
    for i in xrange(len(nums)):
        if nums[i] in num_map and i - num_map[nums[i]] <= k:
            return True
        else:
            num_map[nums[i]] = i
    return False

def containsNearbyDuplicate2(nums, k):
    numDict=dict()
    for x in range(len(nums)):
        idx=numDict.get(nums[x])
        if idx>=0 and x-idx<=k:
            return True
        numDict[nums[x]]=x
    return False