#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 01:11:52 2017

@author: apple
"""

def maxProfit(prices):
    profit=0
    for i in range(1, len(prices)):
        if prices[i]>=prices[i-1]:
            profit+=prices[i]-prices[i-1]
    return profit