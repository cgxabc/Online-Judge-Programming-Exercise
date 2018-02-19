#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:04:56 2018

@author: apple
"""

"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
"""
将整数序列划分为下列区间：

1   1-9   9*1
2   10-99   90*2
3   100-999   900*3
4   1000-9999   9000*4
5   10000-99999
6   100000-999999
7   1000000-9999999
8   10000000-99999999
9   100000000-99999999
"""
"""
思路一：分三步走，

第一步确定是在哪几位数之间
第二步确定是哪个数
第三步确定是这个数的哪一位数
举个例子，比如n=23456，在9+90*2+900*3和9+90*2+900*3+9000*4之间，所以说明，这个数在1000-9999之间，是一个四位数。

一位数时，9*1=9个 
二位数时，90*2=180个， 
三位数时，900*3=2700个， 
。。。。

以此类推，

所以设置long型变量，base代表每位数的个数，9,90,900。。。，ith代表每位数开始的那个数，1,10,100。。。，digit代表几位数，1,2,3。。。这样，循环时，判断n与base*digit的大小，进入n、base、ith、digit的调整。

23456-9-90*2-900*3=20567，

也就是，从1000开始，数20567位，那到底是落在哪个数字上呢？

1000+(20567-1)/4=6141，

所以说，在6141的某一位上，就是第n=23456位数，那到底是哪一位呢？

(20567-1)%4=2，

这说明，在6141的第3位上，也就是4。

注意的是，这里最后计算是哪个数、哪一位时，要减去1，这是因为整除代表某个数的最后一位，所以需要减1。

"""
def findNthDigit(n):
    digit=1   #will become 1,2,3
    base=9   #will become 90, 900
    ith=1  # will become 10, 100,1000
    
    while n>base*digit:  #9, 90*2, 900*3
        n-=base*digit
        digit+=1
        ith*=10
        base*=10
    
    return ord(str(ith+(n-1)/digit)[(n-1)%digit])-ord('0')
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    