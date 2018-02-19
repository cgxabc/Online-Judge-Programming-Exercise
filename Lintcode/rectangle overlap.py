#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:57:11 2018

@author: apple
"""

"""
Given two rectangles, find if the given two rectangles overlap or not.

 Notice

l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.

l1 != r2 and l2 != r2

Have you met this question in a real interview? Yes
Example
Given l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0], return true

Given l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0], return false
"""

"""
up and down disjoint : compare y
left and right disjoint: compare x

"""



"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param: l1: top-left coordinate of first rectangle
    @param: r1: bottom-right coordinate of first rectangle
    @param: l2: top-left coordinate of second rectangle
    @param: r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        # write your code here
        if (r1.x<l2.x or l1.x>r2.x):
            return False
        if (l1.y<r2.y or l2.y<r1.y):
            return False
        return True