#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:36:51 2018

@author: apple
"""

"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Example
Given the below binary tree:

  1
 / \
2   3
return 6.
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution1:
    """
    @param: root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        Solution.max = -10000000
        if root == None: return 0
        self.maxsum(root)
        return Solution.max
    
    def maxsum(self, root):
        if root == None: return 0
        sum = root.val
        lmax = 0; rmax = 0
        if root.left:
            lmax = self.maxsum(root.left)
            if lmax > 0:
                sum += lmax
        if root.right:
            rmax = self.maxsum(root.right)
            if rmax > 0:
                sum += rmax
        if sum > Solution.max: Solution.max = sum
        return max(root.val, max(root.val + lmax, root.val + rmax))



class Solution2:
    """
    @param: root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        maxSum, _ = self.maxPathHelper(root)
        return maxSum
        
    def maxPathHelper(self, root):
        if root is None:
            return -sys.maxint, 0
        
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        maxpath = max(left[0], right[0], root.val + left[1] + right[1])
        single = max(left[1] + root.val, right[1] + root.val, 0)
        
        return maxpath, single
    
    
class Solution3:
    
    def maxPathSum(self, root):
        # write your code here
        self.ans = None
        self.search(root)
        return self.ans 
        
    def search(self, root):
        if root is None:
            return 0
        leftMax = self.search(root.left)
        rightMax = self.search(root.right)
        self.ans = max(max(leftMax, 0) + max(rightMax, 0) + root.val, self.ans)
        return max(leftMax, rightMax, 0) + root.val
            
       
        
















    
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # write your code here