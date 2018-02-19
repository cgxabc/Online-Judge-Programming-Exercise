#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:22:06 2017

@author: apple
"""

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
"""

def reverseWords(s):
    list_of_words=s.split(' ')
    while ' ' in list_of_words:
        list_of_words.remove(' ')
    list_of_words.reverse()
    return ' '.join(list_of_words)


print reverseWords('the sky is blue')
    