#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:19:42 2018

@author: apple
"""

"""
Implement int sqrt(int x).

Compute and return the square root of x.

Have you met this question in a real interview? Yes
Example
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3
"""

def sqrt(x):
    
    start = 0
    end = x
    while start + 1 < end:
         mid = (start + end) / 2
         if mid**2 == x:
            return mid
         if mid**2 > x:
            end = mid
         else:
             start = mid
        
    if start ** 2 <= x <(start + 1) **2:
        return start
            
    if end ** 2 <= x <(end + 1) **2:
        return end
    
