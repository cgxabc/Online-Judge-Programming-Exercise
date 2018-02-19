#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 00:43:41 2018

@author: apple
"""

"""
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right 
which minimizes the sum of all numbers along its path.

You can only move either down or right at any point in time.
"""

def minPathSum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j > 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0 and i > 0:
                grid[i][j] += grid[i-1][j]
            elif i > 0 and j > 0:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[len(grid) - 1][len(grid[0]) - 1]
    