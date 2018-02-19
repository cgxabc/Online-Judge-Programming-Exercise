#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 09:05:01 2018

@author: apple
"""

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""
def longestConsecutive(nums):
    nums = set(nums)
    ans = 0
    while nums:
        l = r = nums.pop()
        while l - 1 in nums:
            l -= 1
            nums.remove(l)
        while r + 1 in nums:
            r += 1
            nums.remove(r)
            
        ans = max(ans, r - l + 1)
        
    return ans
    
nums=[11,3,5,6,8]
nums.remove(3)
print nums
