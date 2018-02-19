#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 00:45:55 2018

@author: apple
"""

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.


Example
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. 
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
# We use "last" to keep track of the maximum distance that has been reached
# by using the minimum steps "ret", 
#whereas "curr" is the maximum distance
# that can be reached by using "ret+1" steps. 
#Thus,curr = max(i+A[i]) where 0 <= i <= last.

def jump(A):
    steps = 0
    last_max_dist = 0
    cur_max_dist = 0
    for i in range(len(A)):
        if i > last_max_dist:
            last_max_dist = cur_max_dist
            steps += 1
        cur_max_dist = max(cur_max_dist, i+A[i])
    return steps

    
    