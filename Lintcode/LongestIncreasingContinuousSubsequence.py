#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:56:18 2018

@author: apple
"""

"""
Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.
Indices of the integers in the subsequence should be continuous.
 Notice

O(n) time and O(1) extra space.

Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.

"""
class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        return max(self.getLongest(A), self.getLongest(list(reversed(A))))
        
    def getLongest(self, A):
        length, longest = 0, 0
        for index, a in enumerate(A):
            if index == 0 or A[index] < A[index - 1]:
                length = 1
            else:
                length += 1
            longest = max(longest, length)
        return longest
    
    
    
    
class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if len(A)==0 or A is None:
            return 0
        return max(self.getLongest(A), self.getLongest(list(reversed(A))))
        
    def getLongest(self, A):
        length = 1
        max_num = 1
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                length = 1
            else:
                length += 1
            max_num = max(max_num, length)
        return max_num   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    