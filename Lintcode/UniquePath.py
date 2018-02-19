#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 00:44:25 2018

@author: apple
"""
def uniquePaths(self, m, n):
        # write your code here
        if m == 0 or n == 0:
            return 0
            
        sum = [[0]*n]*m
        for i in range(m):
            sum[i][0] = 1
        for j in range(n):
            sum[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                sum[i][j] = sum[i-1][j] + sum[i][j-1]
        return sum[m-1][n-1]
