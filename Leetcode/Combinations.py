#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:41:00 2018

@author: apple
"""

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from itertools import combinations
class Solution1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(combinations(range(1,n+1),k))
    
    
##recursive     
class Solution2(object):
    def combine(self,n,k):
        if k==0:
            return [[]]
        return [pre+[i] for i in range(1,n+1) for pre in self.combine(i-1,k-1)]
    

class Solution3(object):
    def combine(self,n,k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
               ans.append(stack[:])
            if l == k or x > n - k + l + 1:
               if not stack:
                   return ans
               x = stack.pop() + 1
            else:
               stack.append(x)
               x += 1
    
    
