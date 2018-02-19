#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:03:08 2017

@author: apple
"""

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""

def maxArea(height):
    max_area=0
    i=0
    j=len(height)-1
    while (i<j):
        cur_area=(j-i)*min(height[i],height[j])
        max_area=max(cur_area, max_area)
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return max_area