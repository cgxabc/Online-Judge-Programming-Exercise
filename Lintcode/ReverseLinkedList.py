#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 22:28:32 2018

@author: apple
"""
"""



"""





class Solution:

    def reverse(self, head):
        curt = None
        while head != None:
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt