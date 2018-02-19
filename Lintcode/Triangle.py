#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 00:40:38 2018

@author: apple
"""

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

 Notice

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Example
Given the following triangle:

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

"""
"""
时间复杂度： O(2^n)

"""


def minimunTotal(triangle):
    # write your code here
    res = [triangle[0]]
    n = len(triangle)
    for i in range(1, len(triangle)):
        res.append([])
        for j in range(len(triangle[i])):
            if j >= 1 and j < len(triangle[i-1]):
                res[i].append(min(res[i-1][j-1], res[i-1][j]) + triangle[i][j])
            elif j >= 1:
                res[i].append(res[i-1][j-1] + triangle[i][j])
            elif j == 0:
                res[i].append(res[i-1][j] + triangle[i][j])
                    
    minvalue = min(res[n-1])
    return minvalue















