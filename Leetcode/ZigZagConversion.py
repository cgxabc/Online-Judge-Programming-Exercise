#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:20:49 2017

@author: apple
"""

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

def convert(s, numRows):
     if numRows == 1:
            return s
        
     rows = ["" for i in range(numRows)]
        
     direction = -1
     row = 0
     for i in range(len(s)):          
         rows[row]+=s[i]
         if (row == 0 or row==numRows-1):
              direction *= -1
         row+=direction
     
     return rows     
     #return "".join(rows)
 
print convert("PAYPALISHIRING",3)    
#['PAHN', 'APLSIIG', 'YIR']
    
    
def convert2(s, numRows):  
    if numRows == 1:
       return s
    step, zigzag = 2 * numRows - 2, ""
    for i in xrange(numRows):
        for j in xrange(i, len(s), step):
            zigzag += s[j]
            if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                zigzag += s[j + step - 2 * i]
    return zigzag

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    