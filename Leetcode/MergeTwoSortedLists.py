#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:39:46 2017

@author: apple
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
合并后的链表仍然是有序的，可以同时遍历两个链表，
每次选取两个链表中较小值的节点，依次连接起来，就能得到最终的链表。
"""



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        head=cur=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 or l2
        return head.next
    
    
    def mergeTwoLists2(self,l1,l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    