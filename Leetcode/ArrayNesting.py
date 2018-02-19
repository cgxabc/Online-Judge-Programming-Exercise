#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 20:25:36 2017

@author: apple
"""

"""
A zero-indexed array A of length N contains all integers from 0 to N-1. 

Find and return the longest length of set S, 

where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, 

the next element in S should be A[A[i]],

and then A[A[A[i]]]… By that analogy, 

we stop adding right before a duplicate element occurs in S.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 6
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
"""

def arrayNesting(nums):
    
    def search(idx):
        cnt=0
        while nums[idx]>=0:
            cnt+=1
            next=nums[idx]
            nums[idx]=-1
            idx=next
        return cnt
    
    
    ans=0
    for x in range(len(nums)):
        if nums[x]>=0:
            ans=max(ans, search(x))
    return ans


def arrayNesting2(nums):
    n = len(nums)
    main_set = set()
    ans = 0

    for i in range(n):
        if nums[i] not in main_set:
            tmp = 0
            t = nums[i]
            while t not in main_set:
                main_set.add(t)
                tmp += 1
                t = nums[t]
            ans = max(ans, tmp)
        else:
            continue
    return ans

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    