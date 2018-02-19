#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 19:47:29 2018

@author: apple
"""

"""
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

 Notice

The subarray should contain at least one number

Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.

"""
"""
这个题的思路是，因为 两个subarray 一定不重叠

所以必定存在一条分割线

分开这两个 subarrays

所以 最后的部分里：

  max = Integer.MIN_VALUE;

        for(int i = 0; i < size - 1; i++){

            max = Math.max(max, left[i] + right[i + 1]);

        }

        return max;

这里是在枚举 这条分割线的位置

然后 left[] 和 right[] 里分别存的是，某个位置往左的 maximum subarray 和往右的 maximum subarray.


"""
def maxTwoSubArrays(nums):
    n = len(nums)
    a = nums[:]
    aa = nums[:]
    for i in range(1, n):
        a[i] = max(nums[i], a[i-1] + nums[i])
        aa[i] = max(a[i], aa[i-1])
    b = nums[:]
    bb = nums[:]
    for i in range(n-2, -1, -1):
          b[i] = max(b[i+1] + nums[i], nums[i])
          bb[i] = max(b[i], bb[i+1])
    mx = -65535
    for i in range(n - 1):
        mx = max(aa[i]+b[i+1], mx)

    return mx








    