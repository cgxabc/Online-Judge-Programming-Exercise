#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:23:16 2018

@author: apple
"""

"""
Count characters in a string. Return a hash map which key is character and value is the occurrency of this character.

Example
Given str = "abca", return

{
  "a": 2,
  "b": 1,
  "c": 1
}
"""
def countCharacters(str):
        d={}
        for char in str:
            if char not in d:
                d[char]=1
            else:
                d[char]+=1
        return d