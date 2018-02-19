#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 22:04:35 2018

@author: apple
"""

"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

#recursively（递归）
def reverseList(head):
    new_head=None
    while head:
        p=head
        head=head.next
        p.next=new_head
        new_head=p
    return new_head
       
#iteratively（迭代）
def reverseList2(head):
    if not head or not head.next:
        return head
    p=head.next
    n=self.reverseList(p)
    head.next=None
    p.next=head
    return n
    