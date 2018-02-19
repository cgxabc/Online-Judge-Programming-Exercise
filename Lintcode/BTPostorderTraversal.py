#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:11:05 2018

@author: apple
"""

"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
 

return [3,2,1].
"""
"""
post-order tranversal:
left child, right child, root
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left, self.right=None, None
"""

class Solution1:
    res=[]
    def postorderTraversal(self, root):
        self.res=[]
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if root is None:
            return None
        self.traverse(root.left)
        self.traverse(root.right)
        self.res.append(root.val)
        
        
class Solution2:
      res=[]  
      def postorderTraversal(self, root):
          self.res=[]
          self.traverse(root)
          return self.res
          
      def traverse(self, root):
          if root is None:
              return None
          myStack1=[]
          myStack2=[]
          node=root
          myStack1.append(node)
          while myStack1:
              node=myStack1.pop()
              if node.left:
                  myStack1.append(node.left)
              if node.right:
                  myStack1.append(node.right)
              myStack2.append(node)
          while myStack2:
              self.res.append(myStack2.pop().val)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        