#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:27:09 2017

@author: apple
"""

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes 
along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
           return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))