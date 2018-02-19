#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:19:22 2018

@author: apple
"""

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Given a binary tree as follow:

  1
 / \ 
2   3
   / \
  4   5
The maximum depth is 3.

"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
    
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)      
        return max(leftDepth, rightDepth) + 1
