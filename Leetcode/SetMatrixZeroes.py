#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:10:14 2017

@author: apple
"""

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""



def setZeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    row=[0]*m
    col=[0]*n
    for i in range(m):
        for j in range(n):
            if not matrix[i][j]:
                row[i]=col[j]=1
                               
    for i in range(m):
        if row[i]:
            for j in range(n):
                matrix[i][j]=0
                
    for j in range(n):
        if col[j]:
            for i in range(m):
                matrix[i][j]=0
            
            
            
            
            
            
            
            
            
            
            
            
        