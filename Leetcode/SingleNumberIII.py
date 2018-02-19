#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:24:00 2017

@author: apple
"""

"""
Given an array of numbers nums, 
in which exactly two elements appear only once 
and all the other elements appear exactly twice. 
Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. 
So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant space complexity?
"""
def singleNumber(nums):
    dict_num={}
    for i in range(len(nums)):
        if nums[i] in dict_num:
            dict_num[nums[i]]+=1
        else:
            dict_num[nums[i]]=1
    a=[]
    for num in dict_num:
        if dict_num[num]==1:
            a.append(num)
    return a


def singleNumber2(nums):
    a=[]
    for i in range(len(nums)):
        if nums[i] in a:
           a.remove(nums[i])
        else:
            a.append(nums[i])      
    return a



def singleNumber3(nums):
        one = set()
        double = set()
        for n in nums:
            if n not in one:
                one.add(n)
            else:
                double.add(n)
        return list(one - double)



def singleNumber4(nums):
        diff = 0
        for n in nums:
            diff ^= n
        #Get its last set bit
        diff &= -diff

        res = [0, 0]
        for n in nums:
            if(n&diff==0):
                res[0] ^= n
            else:
                res[1]^=n

        return res















            
       