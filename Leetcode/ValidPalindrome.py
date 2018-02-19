#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:32:08 2017

@author: apple
"""

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""
def isPalindrome(s):
    start, end=0, len(s)-1
    while start<end:
        while start<end and not s[start].isalpha() and not s[start].isdigit():
            start+=1
        while start<end and not s[end].isalpha() and not s[end].isdigit():
            end-=1
        if start<end and s[start].lower()!=s[end].lower():
            return False
        start+=1
        end-=1
    return True