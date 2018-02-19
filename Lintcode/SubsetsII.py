#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:06:57 2018

@author: apple
"""

"""
Given a list of numbers that may has duplicate numbers, return all possible subsets

 Notice
Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

def subsetsWithDup(self, nums):
    if nums is None:
        return [[]]
    nums.sort()
    ans=[]
    subset=[]
    self.helper(ans, subset, nums, 0)
    return ans
    
    
def helper(self, ans, subset, nums, index):
    ans.append(list(subset))
    for i in range(index, len(nums)):
        if i!=index and nums[i]==nums[i-1]:
            continue
        subset.append(nums[i])
        self.helper(ans,subset,nums,i+1)
        subset.pop()
            
    
# Time:  O(n * 2^n)
# Space: O(1)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
