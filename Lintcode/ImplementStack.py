#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:02:32 2018

@author: apple
"""

"""
Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

Example
push(1)
pop()
push(2)
top()  // return 2
pop()
isEmpty() // return true
push(3)
isEmpty() // return false
"""

class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.items=[]
        
    def push(self, x):
        # write your code here
        self.items.append(x)
    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.items.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.items[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.items)==0
