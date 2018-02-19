#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:05:54 2018

@author: apple
"""

"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_word={}
        for i in s:
            if i not in dict_word.keys():
                dict_word[i]=1
            else:
                dict_word[i]+=1
                
        count = 0
        for i in dict_word.values():
            if i%2 !=0:
                count+=1
            if count > 1:
                return False
        return True
        