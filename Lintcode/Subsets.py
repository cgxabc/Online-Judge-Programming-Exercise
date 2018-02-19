#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:30:17 2018

@author: apple
"""

"""
Given a set of distinct integers, return all possible subsets.

 Notice
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
def subsets1(nums):
    count=1<<len(nums)
    res=[]
    for i in range(count):
        cur=[]
        for j in range(len(nums)):
            if i&(1<<j):
                cur.append(nums[j])
        res.append(sorted(cur))
    return res


def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    if nums is None:
        return [[]]
            
    nums.sort()
    ans = []
    subset = []
    self.helper(ans, subset, nums, 0)
    return ans
    
def helper(self, ans, subset, nums, index):
    ans.append(list(subset))
        
    for i in range(index, len(nums)):
        subset.append(nums[i])
        self.helper(ans, subset, nums, i + 1)
        subset.pop()

       
        
#cur=[4,3]
#print sorted(cur)  
#[3,4]   

        
# Time:  O(n * 2^n)
# Space: O(1)



