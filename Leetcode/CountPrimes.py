#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:33:32 2017

@author: apple
"""

"""
Count the number of prime numbers less than a non-negative number, n.
"""
def countPrimes(n):
    if n <3:
       return 0

    digits=[1]*n
    digits[0]=digits[1]=0
    for i in xrange(2, int(n**0.5)+1):
        if digits[i]==1:
            for j in xrange(i+i,n,i):
                digits[j]=0
    return sum(digits)