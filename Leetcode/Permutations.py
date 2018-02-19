#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 22:41:05 2018

@author: apple
"""

"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

def permute(nums):
    if len(nums)==0: return []
    if len(nums)==1: return [nums]
    res=[]
    for i in range(len(nums)):
        for j in self.permute(nums[:i]+nums[i+1:]):
            res.append([nums[i]]+j)
    return res

def permute2(nums):
    if len(nums) <= 1: return [nums]
    ans = []
    for i, num in enumerate(nums):
        n = nums[:i] + nums[i+1:]
        for y in self.permute(n):
            ans.append([num] + y)
    return ans
















    