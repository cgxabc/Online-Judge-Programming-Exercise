#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 22:40:01 2018

@author: apple
"""

"""
Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.


Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]
"""
def removeElement(A, elem):
    cur=0
    for i in A:
        if i!=elem:
            A[cur]=i
            cur+=1
    return cur