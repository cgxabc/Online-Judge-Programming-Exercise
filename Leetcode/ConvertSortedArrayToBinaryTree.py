#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:54:19 2017

@author: apple
"""

"""
Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is 
defined as a binary tree in which the depth of the two subtrees 
of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], 
which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 
"""

"""
解题思路：由于要求二叉查找树是平衡的。
所以我们可以选在数组的中间那个数当树根root，
然后这个数左边的数组为左子树，右边的数组为右子树，
分别递归产生左右子树就可以了。
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, num):
        length=len(nums)
        if length==0:
            return None
        if length==1:
            return TreeNode(nums[0])
        root=TreeNode(nums[length/2])
        root.left=self.sortedArrayToBST(nums[:length/2])
        root.right=self.sortedArrayToBST(nums[length/2+1:])
        return root







































