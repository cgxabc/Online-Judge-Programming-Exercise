#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:16:03 2017

@author: apple
"""

"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

"""

"""
事实上，可以不用计算两个链表的长度，
因为本质上我们关心的是让两个链表的指针同时到达交叉点。
我们可以定义两个指针，让它们都将两个链表都遍历一遍，
那么它们走的总长度是一样的，倘若两个链表相交，
那么这两个指针一定会在某个地方相等。
"""



def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None
    
    pa=headA
    pb=headB
    while pa is not pb:
        if pa is None:
            pa=headB
        else:
            pa=pa.next
        if pb is None:
            pb=headA
        else:
            pb=pb.next
    return pa
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    