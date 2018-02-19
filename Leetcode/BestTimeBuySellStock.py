#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:58:34 2017

@author: apple
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""
"""
解题思路：扫描一遍数组，使用low来标记最低价位，如果有更低的价位，置换掉。
"""
def maxProfit(prices):
    if len(prices)<=1:
        return 0
    low=prices[0]
    maxprofit=0
    for i in range(len(prices)):
        if prices[i]<low: low=prices[i]
        maxprofit=max(maxprofit, prices[i]-low)
    return maxprofit
    