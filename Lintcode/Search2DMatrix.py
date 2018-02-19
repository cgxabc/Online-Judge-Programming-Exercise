#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:46:43 2018

@author: apple
"""

"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

"""
def searchMatrix1(matrix, target):
    if matrix is None or len(matrix)==0:
        return False
    row=len(matrix)
    col=len(matrix[0])
# find the row index    
    start, end=0, row-1
    while start + 1 < end:
        mid = start + (end - start)/2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            start = mid
        else:
            end = mid
            
    if matrix[end][0] <= target:
        row = end
    elif matrix[start][0] <= target:
        row = start
    else:
        return False
    
# find the column index, the number equal to target
    start = 0
    end = col - 1
    while start + 1 < end:
        mid = start + (end - start)/2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            start = mid
        else:
            end = mid
    
    if matrix[row][start] == target:
        return True
    elif matrix[row][end] == target:
        return True
    
    return False



def searchMatrix2(matrix, target):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    
    