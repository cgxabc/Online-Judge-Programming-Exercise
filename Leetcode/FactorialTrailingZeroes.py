#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:59:14 2017

@author: apple
"""

"""
Given an integer n, return the number of trailing zeroes in n!.
"""

def trailingZeroes(n):
    num_five=0
    while (n):
        num_five+=n/5
        n/=5
    return num_five