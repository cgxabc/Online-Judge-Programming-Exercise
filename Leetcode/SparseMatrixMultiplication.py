#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:01:43 2017

@author: apple
"""

"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

"""
#res=[[0 for _ in xrange(3)] for _ in xrange(5)]
#res2=[[0]*3 for i in xrange(5)]
#print res 
def multiply(A, B):
    m=len(A)  #number of rows of A
    n=len(A[0]) #number of columns of A
    l=len(B[0]) #number of columns of B
    res=[[0 for i in xrange(l)] for j in xrange(m)]
    for i in xrange(m):
        for k in xrange(n):
            if A[i][k]:
                for j in xrange(l):
                    res[i][j]+=A[i][k]*B[k][j]
    return res
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    