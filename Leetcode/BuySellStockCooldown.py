#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:11:57 2017

@author: apple
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
def maxProfit(prices):
    if not prices or len(prices)<2: return 0
    n=len(prices)
    buy, sell=[0]*n, [0]*n
    buy[0]=-prices[0]
    buy[1]=max(-prices[0],-prices[1])
    sell[1]=max(0, prices[1]-prices[0])
    for i in xrange(2,n):
        buy[i]=max(buy[i-1],sell[i-2]-prices[i])
        sell[i]=max(buy[i-1]+prices[i],sell[i-1])
    return sell[n-1]


print maxProfit([1,2,3,0,2])
    