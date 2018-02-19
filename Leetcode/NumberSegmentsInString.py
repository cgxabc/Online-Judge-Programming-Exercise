#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:37:49 2017

@author: apple
"""

"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

def countSegments(s):
    return len(s.split())
    
    