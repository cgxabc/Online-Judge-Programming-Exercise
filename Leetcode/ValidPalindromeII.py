#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:32:53 2018

@author: apple
"""

"""
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:
    
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. 
The maximum length of the string is 50000.
"""
s='abca'
s_minus=s[:2]+s[3:]
#print s_minus[::-1]



def validPalindrome(s):
    isPalindrome = lambda s: s == s[::-1]
    strPart = lambda s, x: s[:x] + s[x + 1:]
    size = len(s)
    lo, hi = 0, size - 1
    while lo < hi:
        if s[lo] != s[hi]:
           return isPalindrome(strPart(s, lo)) or isPalindrome(strPart(s, hi))
        lo += 1
        hi -= 1
    return True
    
#def validPalindrome2(s):  #does not work
 #   if s[::-1]==s:
  #      return True
  #  for i in range(len(s)-1):
   #     s_minus=s[:i]+s[i+1:]
    #    if s_minus!=s_minus[::-1]:
      #      return False
  #  return True
    
#isPalindrome = lambda s: s == s[::-1]    
#print isPalindrome('erre')    
#print validPalindrome('eccer')










