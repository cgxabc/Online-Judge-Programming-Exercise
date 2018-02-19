#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 21:28:12 2017

@author: apple
"""

"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
"""
"""
根据题意，不能有超过连续两根柱子是一个颜色，
也就意味着第三根柱子要么根第一个柱子不是一个颜色，
要么跟第二根柱子不是一个颜色。
如果不是同一个颜色，计算可能性的时候就要去掉之前的颜色，
也就是k-1种可能性。假设dp[1]是第一根柱子及之前涂色的可能性数量，
dp[2]是第二根柱子及之前涂色的可能性数量，
则dp[3]=(k-1)*dp[1] + (k-1)*dp[2]。
"""
def numWays(n, k):
    if n==0:
        return 0
    elif n==1:
        return k
    dp=[0]*n
    dp[0]=k
    dp[1]=k*k
    for i in xrange(2,n):
        dp[i]=(k-1)*(dp[i-1]+dp[i-2])
    return dp[n-1]
       