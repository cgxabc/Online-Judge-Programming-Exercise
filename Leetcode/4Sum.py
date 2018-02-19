#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:08:43 2017

@author: apple
"""

"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""
def fourSum(nums, target):
    solution_set=[]
    nums.sort()
    for i in range(0, len(nums)-3):
        for j in range(i+1, len(nums)-2):
            p=j+1
            q=len(nums)-1
            while p!=q:
                temp_sum=nums[i]+nums[j]+nums[p]+nums[q]
                if temp_sum==target:
                    solution=[nums[i],nums[j], nums[p], nums[q]]
                    if solution not in solution_set:
                        solution_set.append(solution)
                    p+=1
                    
                elif temp_sum>target:
                    q-=1
                else:
                    p+=1
    return solution_set
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    