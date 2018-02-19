#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 23:54:17 2017

@author: apple
"""

"""
Say you have an array for which 
the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete at most two transactions.
"""

"""
解题思路：只允许做两次交易，这道题就比前两道要难多了。
解法很巧妙，有点动态规划的意思：
开辟两个数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得的最大利润，
f2[i]表示在price[i]之后进行一次交易所获得的最大利润。
则f1[i]+f2[i]的最大值就是所要求的最大值，
而f1[i]和f2[i]的计算就需要动态规划了，看代码不难理解。

"""

def maxProfit(prices):
    length=len(prices)
    if length==0: return 0
    f1=[0 for i in range(length)]
    f2=[0 for i in range(length)]
        
    minV=prices[0]; f1[0]=0
    for i in range(1,length):
        minV=min(minV, prices[i])
        f1[i]=max(f1[i-1],prices[i]-minV)
            
    maxV=prices[length-1]; f2[length-1]=0
    for i in range(length-2,-1,-1):
        maxV=max(maxV,prices[i])
        f2[i]=max(f2[i+1],maxV-prices[i])
        
    res=0
    for i in range(length):
        if f1[i]+f2[i]>res: res=f1[i]+f2[i]
    return res


def maxProfit2(prices):
    if not prices : return 0
    n = len(prices)
    dp , money,profit=[],prices[0],0
    for i in range(n):
        profit = max(profit,prices[i]-money)
        money = min(money,prices[i])
        dp.append(profit)
        
    i ,ans ,money,profit= n - 1 , dp[n-1],prices[n-1],0
    while i >=0:
        profit = max(profit,money-prices[i])
        money = max(money,prices[i])
        ans=max(ans,dp[i]+profit)
        i-=1
    return ans





















