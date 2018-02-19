#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:55:40 2017

@author: apple
"""

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 
 
"""
#class ListNode(object):
    #def __init__(self, x):
       # self.val=x
       # self.next=None
        
#class TreeNode(object):
    #def __init__(self, x):
      #  self.val=x
      #  self.left=None
       # self.right=None
        
class Solution1(object):
    def sortedListToBST(self, head):
        current, length=head, 0
        while current is not None:
            current, length=current.next, length+1
        self.head=head
        return self.sortedListToBSTRecu(0, length)
    
    def sortedListToBSTRecu(self, start, end):
        if start==end:
            return None
        mid=start+(end-start)/2
        left=self.sortedListToBSTRecu(start, mid)
        current=TreeNode(self.head.val)
        current.left=left
        self.head=self.head.next
        current.right=self.sortedListToBSTRecu(mid+1, end)
        return current
    
    
    
class Solution2(object):
    def sortedListToBST(self, head):
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        return self.helper(0, len(nums)-1, nums)
    
    def helper(self, left, right, nums):
        if left>right:
            return 
        if left==right:
            return TreeNode(nums[left])
        mid=(left+right)/2
        root=TreeNode(nums[mid])
        left=self.helper(left, mid-1, nums)
        right=self.helper(mid+1, right, nums)
        root.left, root.right=left, right
        return root
        
        
        
        
class Solution3(object):     
    def sortedListToBST(self, head):
        cur=head
        if head is None:
            return 
        sortedlist=[]
        while cur is not None:
            sortedlist.append(cur.val)
            cur=cur.next
        head=self.convertToBST(sortedlist)
        return head
    
    def convertToBST(self, sortedlist):
        if len(sortedlist)==0:return None
        mid=int(len(sortedlist)/2)
        root=TreeNode(sortedlist[mid])
        root.left=self.convertToBST(sortedlist[:mid])
        root.right=self.convertToBST(sortedlist[mid+1:])
        return root
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
        





























