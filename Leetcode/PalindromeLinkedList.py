#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 00:02:50 2017

@author: apple
"""

"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        cur=slow.next
 
        pre=None
        #reverse the second half
        while cur:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        #compare values from two halves
        tail=pre
        while head and tail:
            if head.val!=tail.val:
                return False
            head=head.next
            tail=tail.next
        return True
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            