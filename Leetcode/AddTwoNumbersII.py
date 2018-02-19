#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 11:05:53 2018

@author: apple
"""

"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

def addTwoNumbers(l1, l2):
    stk1, stk2=[], []
    sum=0
    while l1:
        stk1.append(l1.val)
        l1=l1.next
    while l2:
        stk2.append(l2.val)
        l2=l2.next
    
    prev, head=None, None
    while stk1 or stk2:
        sum/=10
        if stk1:
            sum+=stk1.pop()
        if stk2:
            sum+=stk2.pop()
        head=ListNode(sum%10)
        head.next=prev
        prev=head
        
    if sum>=10:
        head=ListNode(sum/10)
        head.next=prev
    return head
        