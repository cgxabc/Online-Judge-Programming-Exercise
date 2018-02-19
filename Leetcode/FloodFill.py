#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:41:12 2018

@author: apple
"""

"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

def floodFill1(image, sr, sc, newColor):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    queue = [(sr, sc)]
    oldColor = image[sr][sc]
    image[sr][sc] = newColor
    while queue:
        x, y = queue.pop(0)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
                if image[nx][ny] != newColor and image[nx][ny] == oldColor:
                    image[nx][ny] = newColor
                    queue.append((nx, ny))
    return image


def floodFill2(image, sr, sc, newColor):
    rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
    def traverse(row, col):
        if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
            return
        image[row][col] = newColor
        [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
    if orig_color != newColor:
        traverse(sr, sc)
    return image
    
    
    
print False or False    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    