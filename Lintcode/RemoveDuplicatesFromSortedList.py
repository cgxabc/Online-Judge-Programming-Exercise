#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 22:22:10 2018

@author: apple
"""

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return None
            
        node=head
        while node.next is not None:
            if node.val==node.next.val:
                node.next=node.next.next
            else:
                node=node.next
        return head
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    