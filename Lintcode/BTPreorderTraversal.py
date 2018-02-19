#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:06:44 2018

@author: apple
"""

"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example
Given:

    1
   / \
  2   3
 / \
4   5
return [1,2,4,5,3].
"""
"""
pre-order traversal: parent, left, right
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left, self.right=None, None
"""
class Solution1:
    res=[]
    def preorderTraversal(self, root):
        self.res=[]
        self.transverse(root)
        return self.res
        
    def transverse(self, root):
        if root is None:
            return None
        myStack=[]
        node=root
        while node or myStack:
             while node:
                 self.res.append(node.val)
                 myStack.append(node)
                 node=node.left
             node=myStack.pop()
             node=node.right
             
             
             
class Solution2:
    res=[]
    def preorderTraversal(self, root):
        self.res=[]
        self.transverse(root)
        return self.res
    
    def transverse(self, root):
        if root is None:
            return None
        self.res.append(root.val)
        self.transverse(root.left)
        self.transverse(root.right)
        
        
        
        
        
        
        
            
        
        