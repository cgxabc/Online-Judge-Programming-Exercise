#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:02:18 2017

@author: apple
"""

"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def merge(intervals):
    intervals.sort(key=lambda x: x.start)
    length=len(intervals)
    res=[]
    for i in range(length):
        if res==[]:
            res.append(intervals[i])
        else:
            size=len(res)
            if res[size-1].start<=intervals[i].start<=res[size-1].end:
                res[size-1].end=max(intervals[i].end, res[size-1].end)
            else:
                res.append(intervals[i])
    return res


def merge2(intervals):
    if not intervals:
        return intervals
    intervals.sort(key=lambda x: x.start)
    result=[intervals[0]]
    for i in xrange(1,len(intervals)):
        prev, current=result[-1], intervals[i]
        if current.start<=prev.end:  #[3,5] , [4,8]
            prev.end=max(prev.end, current.end)
        else:
            result.append(current)
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    