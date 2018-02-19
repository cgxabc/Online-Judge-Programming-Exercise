#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 00:45:33 2018

@author: apple
"""

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 Notice

This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.


Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

"""
def canJump(self, A):
        # write your code here
    can = [False for _ in range(len(A))]
    can[0] = True
    for i in range(1, len(A)):
        for j in range(i):
            if can[j] and j + A[j] >= i:
                can[i] = True
                break
    return can[len(A)-1]


    

























