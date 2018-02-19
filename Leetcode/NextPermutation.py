#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:05:43 2017

@author: apple
"""

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

def nextPermutation(nums):
    k,l=-1,0
    for i in xrange(len(nums)-1):
        if nums[i]<nums[i+1]:
            k=i
    if k==-1:
        nums.reverse()
        return
    
    for i in xrange(k+1, len(nums)):
        if nums[i]>nums[k]:
            l=i
    nums[k], nums[l]=nums[l], nums[k]
    nums[k+1:]=nums[:k:-1]
    return nums

print nextPermutation([1,3,4,19,100,67,21,5])
#[1,3,4,21,100,67,19,5]
#[1,3,4,21,5,19,67,100]



#[1, 3, 4, 21, 5, 19, 67, 100]
   

#def combinationSum(candidates,target):
#nums=[1,3,4,19,8,6,21,5]
#k,l=-1,0
#for i in xrange(len(nums)-1):
  # if nums[i]<nums[i+1]:
      # k=i
       
#for i in xrange(k+1, len(nums)):
      #  if nums[i]>nums[k]:
          #  l=i
       
#print k, l  #5,6

#[1,3,4,19,8,21,6,5]
#[1,3,4,19,8,21,5,6]

















