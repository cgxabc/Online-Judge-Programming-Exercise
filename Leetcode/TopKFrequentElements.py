#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:42:04 2017

@author: apple
"""

def topKFrequent(nums, k):
    dict_num={}
    for i in nums:
        if i in dict_num:
            dict_num[i]+=1
        else:
            dict_num[i]=1
    sorted_dict=sorted(dict_num.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    alist=[]
    for key, value in sorted_dict[:k]:
        alist.append(key)
    return alist

print topKFrequent([1,1,1,2,2,3], 2)
        
    