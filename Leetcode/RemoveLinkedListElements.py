#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:42:59 2017

@author: apple
"""

"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def removeElement(head,val):
    dummy = ListNode(float("-inf"))
    dummy.next = head
    prev, curr = dummy, dummy.next
        
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
            
        curr = curr.next
        
    return dummy.next


def removeElement2(head, val):
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next
















            