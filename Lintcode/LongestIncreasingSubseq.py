#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 00:46:20 2018

@author: apple
"""

"""
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.


Clarification
What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Example
For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4
"""
def longestIncreasingSubsequence(nums):
    if nums is None or len(nums)==0:
            return 0
    f = [1 for _ in range(len(nums))]
    max_num = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                f[i] = max(f[i], f[j]+1)
        max_num = max(max_num, f[i])
    return max_num