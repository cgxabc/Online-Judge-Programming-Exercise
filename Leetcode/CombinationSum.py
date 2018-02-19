#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:06:20 2017

@author: apple
"""

"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
"""
class Solution(object):
  def combinationSum(self, candidates,target):
      candidates.sort()
      solution_set=[]
      self.DFS(candidates, target,0,[])
      return solution_set
  
  def DFS(self,candidates, target, start,valuelist):
      length=len(candidates)
      if target==0:
          return solution_set.append(valuelist)
      for i in range(start, length):
          if target<candidates[i]:
              return
          self.DFS(candidates, target-candidates[i], i,valuelist+[candidates[i]])
          
          


