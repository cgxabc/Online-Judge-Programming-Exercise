#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 00:08:44 2018

@author: apple
"""

"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

 Notice

m and n will be at most 100.

Have you met this question in a real interview? Yes
Example
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

"""
def uniquePathsWithObstacles(self, obstacleGrid):
    if obstacleGrid is None or len(obstacleGrid) == 0 or  len(obstacleGrid[0])== 0:
            return 0
            
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    path_num = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        if obstacleGrid[i][0] != 1:
            path_num[i][0] = 1
        else:
            path_num[i][0] = 0
            break
    for j in range(n):
        if obstacleGrid[0][j] != 1:
            path_num[0][j] = 1
        else:
            path_num[0][j] = 0
            break  
            
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                path_num[i][j] = 0
            else:
                path_num[i][j] = path_num[i-1][j] + path_num[i][j-1]
    return path_num[m-1][n-1]
    

