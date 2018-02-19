#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:04:25 2017

@author: apple
"""

"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. 
You may assume that each word will contain only lower case letters. 
If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""


#时间复杂度O(n2)，空间复杂度
words=['abfds','gkkk','gfgre']
codes=[]
for i in words:
    tmp=0
    for j in list(i):
        tmp|=1<<(ord(j)-ord('a'))
     
    codes.append(tmp)
tmp1=tmp2=tmp3=tmp4=tmp5=0
tmp1|=1<<(ord('a')-ord('a')) 
print tmp1
tmp2|=1<<(ord('b')-ord('a')) 
print tmp2
tmp3|=1<<(ord('f')-ord('a')) 
print tmp3
tmp4|=1<<(ord('d')-ord('a')) 
print tmp4
tmp5|=1<<(ord('s')-ord('a')) 
print tmp5
print codes[0]&codes[2]

def maxProduct(words):
    
    if not words:
        return 0
    curr_max=0
    while words:
         curr_words=set(words[0])
         curr_len=len(words[0])
         words=words[1:]
         for word in words:
             count=0
             for char in curr_words:
                 if char in word:
                    count=1
                    break
             if not count:
                  curr_max=max(curr_max, curr_len*len(word))
    return curr_max
         
         
         
         
         




def maxProduct2(words):
    nums = []
    size = len(words)
    for w in words:
        nums += sum(1 << (ord(x) - ord('a')) for x in set(w)),
    ans = 0
    for x in range(size):
        for y in range(size):
            if not (nums[x] & nums[y]):
                ans = max(len(words[x]) * len(words[y]), ans)
    return ans















    
              