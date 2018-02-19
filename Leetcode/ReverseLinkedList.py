#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:56:39 2017

@author: apple
"""

"""
Reverse a singly linked list.
"""

def reverseList(head):
    new_head=None
    while head:
        p=head
        head=head.next
        p.next=new_head
        new_head=p
    return new_head


def reverseList(head):
    prev=None
    curr=head
    while curr:
        nextTemp=curr.next
        curr.next=prev
        prev=curr
        curr=nextTemp
    return prev
    
    