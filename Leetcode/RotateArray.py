#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 15:04:26 2017

@author: apple
"""

"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II

"""

def rotate(nums,k):
    nums2=[0]*len(nums)
    for i in range(len(nums)):
       # print (i+k)%len(nums)
        nums2[(i+k)%len(nums)]=nums[i]
    nums=nums2
    return nums
 
def rotate2(nums, k):
    n=len(nums)
    if k>0 and n>1:
        nums[:]=nums[n-k:]+nums[:n-k]
    return nums

def rotate3(nums, k):
    k=k%len(nums)
    n=len(nums)
    for i in range(n-k):
        nums.append(nums[0])
        nums.pop(0)
    return nums



print rotate3([1,2],1)
#[2, 1]