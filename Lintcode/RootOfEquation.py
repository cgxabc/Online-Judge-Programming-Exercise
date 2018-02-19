#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:43:46 2018

@author: apple
"""
"""
Given an equation: ax2 + bx + c = 0. Find the root of the equation.

If there are two roots, return a list with two roots in it.
If there are only one root, return a list with only one root in it.
If there are no root for the given equation, return an empty list.
Have you met this question in a real interview? Yes
Example
Given a = 1, b = -2, c = 1. return [1].

Given a = 1, b = -3, c = 2. return [1, 2]. The first one should smaller than the second.

Given a = 1, b = 1, c = 1. return [].

"""
def rootOfEquation(a, b, c):
    ans=[]
    delta=b**2-4*a*c
    import math
    if delta>0:
        ans.append(float((-b-math.sqrt(delta)))/(2*a))
        ans.append(float((-b+math.sqrt(delta)))/(2*a))
        ans=sorted(ans)
    if delta==0:
        ans.append(float(-b)/(2*a))
        
    return ans


print rootOfEquation(1.0,-2.0,1.0)