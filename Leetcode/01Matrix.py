#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:36:20 2017

@author: apple
"""

"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
"""
初始令step = 0，将matrix中所有1元素加入队列queue

循环，直到queue为空：

  令step = step + 1

  遍历queue中的元素，记当前元素为p，坐标为(x, y)：

    若p的相邻元素中包含0元素，则p的距离设为step，从queue中移除p
    
  将上一步中移除的元素对应的matrix值设为0
"""
def updateMatrix(matrix):
    h=len(matrix) #number of rows
    w=len(matrix[0]) #number of columns
    ans=[[0]*w for x in range(h)]
    queue=[(x,y) for x in range(h) for y in range(w) if matrix[x][y]]
    step=0
    while queue:
        step+=1
        nqueue, mqueue=[],[]
        for x, y in queue:
            zero=0
            for dx, dy in zip((1,0,-1,0),(0,1,0,-1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<h and 0<=ny<w and matrix[nx][ny]==0:
                    zero+=1
            if zero:
                ans[x][y]=step
                mqueue.append((x,y))  #points to remove
            else:
                nqueue.append((x,y))  #points to keep for next round
        for x,y in mqueue:
            matrix[x][y]=0
        queue=nqueue  #for next round
    return ans
                    
                




















