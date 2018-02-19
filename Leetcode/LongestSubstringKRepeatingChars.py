#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:54:41 2017

@author: apple
"""

"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

def longestSubstring(s,k):
    cnt=collections.Counter(s)
    filters=[x for x in cnt if cnt[x]<k]
    if not filters:
        return len(s)
    tokens=re.split('|'.join(filters), s)
    return max(self.longestSubstring(t, k) for t in tokens)


#import collections
#import re
#s='aabbbfffe'
#cnt=collections.Counter(s)
#filters=[x for x in cnt if cnt[x]<3]
#tokens=re.split('|'.join(filters), s)
#print cnt  #Counter({'b': 3, 'f': 3, 'a': 2, 'e': 1})
#print filters  #['a', 'e']
#print tokens  #['', '', 'bbbfff', '']






















