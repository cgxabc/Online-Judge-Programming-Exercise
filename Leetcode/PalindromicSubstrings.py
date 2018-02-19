#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:22:30 2017

@author: apple
"""

"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""
"""
找到字符串中的回文子序列的个数 
比如 给定一个字符串“aaa”, 它的子序列的个数就是 a, a, a, aa, aa, aaa 
如果给定的是“abc”, 那么它的子序列就是a, b, c

string[i]到 string[j] 这个子串是回文的可能性只有当 string[i] == string[j] 而且string[i + 1] 到 string[j - 1] 是回文。 但是考虑到如果中间只有一个字符时它一定是回文，所以我的判断条件写的是 i +1 >= j - 1。

如果中间不止一个字符时，那么就通过判断 dp[i + 1][j - 1] 是不是 >= 0。因为dp[i + 1][j - 1] 是前面的中间结果，所以这里可以直接判断。

最后的算法如下： 
从 string[0][1] 开始循环到 string[0][n]。 
对于 substring string[i][j], 如果它是回文的，那么就count ++， dp[i][j] = 1 
最后返回count 即可。
"""

def countSubstring(s):
    length=len(s)
    dp=[[0]*length for i in xrange(length)]
    count=0
    for end in xrange(length):
        dp[end][end]=1
        count+=1
        for start in xrange(end):
            if(s[start]==s[end] and (start+1>=end-1 or dp[start+1][end-1])):
                count+=1
                dp[start][end]=1
    return count
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
  
