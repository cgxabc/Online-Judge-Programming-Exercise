#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:04:46 2017

@author: apple
"""

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

"""

#Boyer–Moore majority vote algorithm



def majorityElement(nums):
    n1=n2=None
    c1=c2=0
    for num in nums:
        if n1==num:
            c1+=1
        elif n2==num:
            c2+=1
        elif c1==0:
            n1=num
            c1=1
        elif c2==0:
            n2=num
            c2=1
        else:
            c1=c1-1
            c2=c2-1
    return [n for n in (n1,n2) if n is not None and nums.count(n)>len(nums)/3]


print majorityElement([2,2,4,4,3,3,3])