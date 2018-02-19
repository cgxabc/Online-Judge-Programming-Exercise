#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 00:44:05 2017

@author: apple
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in s:
            sum=sum*26+ord(i)-64
        return sum