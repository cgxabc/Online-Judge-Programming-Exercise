#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 23:54:33 2017

@author: apple
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""

"""
dp,设dp[i][j]为第J天进行第i次交易能获取的最大值。

当k >=n/2时候，相当于第122题。Best Time to Buy and Sell Stock II
dp[i][j]=max(dp[i][j-1],prices[j] + maxTemp)  
我们能获取的最大利润，当我们在第j天进行抛售时。由于maxTemp已经算了买进时的价格，所以直接加上即可。
maxTemp =max(maxTemp,dp[i-1][j-1] – prices[j])  
可以理解为已获得的最大利润，即如果买进第j天的，
那么用之前一轮的买卖，前一天的的利润即（dp[i-1][j-1]）减去prices[j]

"""


class Solution(object):
    def maxProfit(self, k, prices):
        n=len(prices)
        if k>n/2:
            return self.maxProfit2(prices)
        dp=[[0]*n for i in xrange(k+1)]  
        #dp[i] indicates maximum profits of having i trades during each of n days.
        for i in xrange(1, k+1):
            maxTemp=-prices[0]
            for j in xrange(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j]+maxTemp)
                maxTemp=max(maxTemp, dp[i-1][j-1]-prices[j])
        return dp[k][n-1]
        
        
        
    def maxProfit2(self, prices):
        ans=0
        for i in xrange(1, len(prices)):
            if prices[i]>prices[i-1]:
                ans+=prices[i]-prices[i-1]
        return ans


























