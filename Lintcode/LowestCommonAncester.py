#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:54:06 2018

@author: apple
"""

"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

Assume two nodes are exist in tree.

Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7

"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None
        if root == A or root == B:
            return root
    #Divide      
        left = self.lowestCommonAncestor(root. left, A, B)
        right = self.lowestCommonAncestor(root. right, A, B)
    #Conquer
        if left != None and right != None:
            return root
        if left != None:
            return left
        if right!= None:
            return right
        return None
        
# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

#dis=Solution()
#print dis.lowestCommonAncestor(root, 4, 5)
#print "LCA(4, 5) = %d" %(dis.lowestCommonAncestor(root, 4, 5))


#print "LCA(4, 6) = %d" %(lowestCommonAncestor(root, 4, 6))
#print "LCA(3, 4) = %d" %(lowestCommonAncestor(root,3,4))
#print "LCA(2, 4) = %d" %(lowestCommonAncestor(root,2, 4))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
