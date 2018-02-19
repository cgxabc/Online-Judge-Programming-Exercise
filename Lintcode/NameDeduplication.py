#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:18:13 2018

@author: apple
"""

"""
Given a list of names, remove the duplicate names. Two name will be treated as the same name if they are equal ignore the case.

Return a list of names without duplication, all names should be in lowercase, and keep the order in the original list.

Example
Given:

["James", "james", "Bill Gates", "bill Gates", "Hello World", "HELLO WORLD", "Helloworld"]
return:

["james", "bill gates", "hello world", "helloworld"]
"""
def nameDeduplication(names):
    d={}
    result=[]
    for name in names:
        name=name.lower()
        if name not in d:
            d[name]=1
            result.append(name)
    return result
    