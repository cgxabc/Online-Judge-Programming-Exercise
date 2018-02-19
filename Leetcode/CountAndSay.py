#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:25:16 2018

@author: apple
"""

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

def countAndSay1(n):
    res = '1'
    for i in xrange(n-1):
        new_res = ''
        j = 0
        while j < len(res):
            count = 1
            while j < len(res)-1 and res[j] == res[j+1]:
                j = j + 1
                count = count + 1
            j = j + 1
            new_res = new_res + str(count) + res[j-1]
        res = new_res
    return res




def countAndSay2(n):
     res = '1'
     for i in xrange(n-1):
         new_res, pre, count = '', res[0], 0
         for j in xrange(len(res)):
             if res[j] == pre:
                 count += 1
             else:
                 new_res += str(count) + pre
                 count = 1
                 pre = res[j]
         res = new_res + str(count) + pre
     return res



def countAndSay3(n):
    res = '1'
    for i in xrange(n-1):
        res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
    return res
































    