
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 00:20:02 2017

@author: apple
"""

"""
There are 1000 buckets, one and only one of them contains poison, 
the rest are filled with water. They all look the same. 
If a pig drinks that poison it will die within 15 minutes. 
What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:

If there are n buckets and a pig drinking poison will die within m minutes, 
how many pigs (x) you need to figure out the "poison" bucket within p minutes? 
There is exact one bucket with poison.

"""
"""
buckets = pow(r + 1, n)
n = log(buckets, r + 1)

如果只有一只猪，考虑到间隔时间为15分钟，而测试时间是60分钟，所以一维的情况下，一只猪可以测出最多五只桶(为什么不是60/15, 4只呢，因为如果前面四个测试猪都没有死，则证明第五只桶有毒，但是不能六只桶，因为四次测试时间用完，会剩下两只，无法确定哪只有毒)。也就是说如果只有一只猪，可以最多检查(测试时间/毒发时间 + 1)个桶。

扩展到二维，则2只猪可以检查出5*5个桶，3个猪就是5^3个桶，因此到最后就是使用pow函数来和桶数进行比较。

"""



def poorPigs(buckets, minutesToDie, minutesToTest):
    return int(math.ceil(math.log(buckets, 1 + minutesToTest / minutesToDie)))


def poorPigs2(buckets, minutesToDie, minutesToTest):
    time = minutesToTest/minutesToDie + 1
    res = 0
    while(math.pow(time, res)< buckets):
        res+=res

    return res

