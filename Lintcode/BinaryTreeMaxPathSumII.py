#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 18:20:57 2018

@author: apple
"""

"""
Given a binary tree, find the maximum path sum.

The path may end at any node in the tree and contain at least one node in it.

Example
Given the below binary tree:

  1
 / \
2   3
return 4 (1->3).
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
def maxPathSum2(self, root):
    if root is None:
        return 0
    left = self.maxPathSum2(root.left)
    right = self.maxPathSum2(root.right)
    
    return max(0, max(left, right)) + root.val
    
