#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:04:09 2018

@author: apple
"""

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
 

return [1,3,2].
"""

"""
Inorder Traversal: left, parent, right
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
    def inorderTraversal(self, root):
        self.res=[]
        self.transverse(root)
        return self.res
        
    def transverse(self, root):
        if root is None:
            return None
        self.transverse(root.left)
        self.res.append(root.val)
        self.transverse(root.right)
        
        
        
        
        
        
class Solution2:
    res=[]
    def inorderTraversal(self, root):
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
                myStack.append(node)
                node=node.left
            node=myStack.pop()
            self.res.append(node.val)
            node=node.right
        
        
        
        
        
        
        
        
        
        
        
        
        