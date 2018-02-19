#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:30:39 2017

@author: apple
"""

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

#def findDisappearedNumbers(nums):
  #  num_dis=[]
   # for i in range(1, len(nums)+1):
     #   if i not in nums:
          #  num_dis.append(i)
  #  return num_dis



def findDisappearedNumbers2(nums):
     for i in range(len(nums)):
         index=abs(nums[i])
         nums[index]=-abs(nums[index])
     return [i+1 for i in range(len(nums)) if nums[i]>0]
         






print findDisappearedNumbers([4,3,2,7,8,2,3,1])