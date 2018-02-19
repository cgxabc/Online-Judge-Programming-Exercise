#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:21:30 2017

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
import collections
import re
def longestSubstring(s, k):
    cnt=collections.Counter(s)
    filters=[x for x in cnt if cnt[x]<k]
    if not filters:
        return len(s)
    tokens=re.split('|'.join(filters), s)
    return max(self.longestSubstring(t,k) for t in tokens)


#s='aaaabbnnnfff'
#k=3
#cnt=collections.Counter(s)
#filters=[x for x in cnt if cnt[x]<k]
#print filters
#['b']

#tokens=re.split('|'.join(filters),s)
#print tokens
#['aaaa', '', 'nnnfff']

#tokens2=re.split('|',s)
#print tokens2
#['aaaabbnnnfff']


















