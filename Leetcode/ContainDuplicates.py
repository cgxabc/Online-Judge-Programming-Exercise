#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:10:14 2017

@author: apple
"""

"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

"""

def containDuplicate(nums):
    dictNum={}
    for i in nums:
        if i in dictNum:
            return True
        else:
            dictNum[i]=True
    return False
        