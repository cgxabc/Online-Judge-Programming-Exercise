#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:33:27 2017

@author: apple
"""

"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""
#def replaceWords(dict, sentence):
#sentence = "the cattle was rattled by the battery"
#s=sentence.split()
#print s[1].startswith('cat')
#True
def replaceWords(dict, sentence):
    sentence=sentence.split()
    dict_replace={}
    for word in sentence:
        dict_replace[word]=[]
        for root in dict:
            if word.startswith(root):
                dict_replace[word].append(root)
    #return dict_replace
    
                
    for i in range(len(sentence)):
        if dict_replace[sentence[i]]!=[]:
            shortest_length=len(dict_replace[sentence[i]][0])
            for root in dict_replace[sentence[i]]:
                shortest_length=min(shortest_length,len(root))
            
            for root in dict_replace[sentence[i]]:
                if len(root)==shortest_length:
                    sentence[i]=root
                    
    return " ".join(x for x in sentence)


print replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
            
       
            
    
    
