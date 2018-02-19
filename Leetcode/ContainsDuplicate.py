#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:41:16 2017

@author: apple
"""

"""
Given an array of integers, 
find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
"""
def containsDuplicate(nums):
    for i in nums:
        nums.remove(i)
        if i in nums:
            return True
        
    return False


def containsDuplicate2(nums):
    nums.sort()
    for i in xrange(0, len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False

def containsDuplicate3(nums):
    dictNum={}
    for i in nums:
        if i in dictNum:
            return True
        else:
            dictNum[i]=True
    return False

def containsDuplicate4(nums):
    return len(nums) != len(set(nums))



print containsDuplicate2([5,1,2,3])