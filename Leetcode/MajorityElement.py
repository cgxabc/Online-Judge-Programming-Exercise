#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:11:33 2017

@author: apple
"""
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""



def majorityElement(nums):
     dictNum={}
     if len(nums)==1:
         return nums[0]
     else:
         for num in nums:
             if dictNum.has_key(num):
                if dictNum[num]>=len(nums)/2:
                     return num
                else: 
                     dictNum[num]+=1
             else:
                    dictNum[num]=1
  
        
                