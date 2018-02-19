#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:55:45 2018

@author: apple
"""

"""
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.

Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.
"""
def searchMatrix(matrix, target):
    if matrix == [] or matrix[0] == []:
        return 0
            
    row, column = len(matrix), len(matrix[0])
    i, j = row - 1, 0
    count = 0
    while i >= 0 and j < column:
        if matrix[i][j] == target:
            count += 1
            i -= 1
            j += 1
        elif matrix[i][j] < target:
            j += 1
        elif matrix[i][j] > target:
            i -= 1
    return count