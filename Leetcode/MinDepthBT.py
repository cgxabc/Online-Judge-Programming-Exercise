#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 07:52:16 2018

@author: apple
"""

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

"""
#Definition for a binary tree node
#class TreeNode(object):
#   def __init__(self,x):
#       self.val=x
#       self.left=None
#       self.right=None

class Solution1(object):
    def minDepth(self, root):
        if root==None:
            return 0
        if root.left==None and rrot.right!=None:
            return self.minDepth(root.right)+1
        if root.left!=None and root.right==None:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
    
    
class Solution2(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue=[]
        queue.append(root)
        level=0
        
        