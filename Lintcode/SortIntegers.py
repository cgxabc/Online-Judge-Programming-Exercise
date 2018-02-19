#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:18:28 2018

@author: apple
"""

"""
Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

Example
Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].

"""
"""
bubble sort
"""
def sortIntegers1(A):
    if len(A)==0:
        return 
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                
                
"""
selection sort
"""

def sortInteger2(A):
    for i in range(len(A)-1):
        index=i
        for j in range(i+1, len(A)):
            if A[index]>A[j]:
                index=j
        A[index], A[i]=A[i], A[index]
        
        
"""
insertion sort
"""
def sortInteger3(A):
   for i in range(len(A)):
      key=A[i]
      j=i-1
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position    
      while (j>-1 and A[j]>key):
          A[j+1]=A[j]
          j-=1
      A[j+1]=key
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    