#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:53:16 2018

@author: apple
"""

"""
Factory is a design pattern in common usage. Implement a ShapeFactory that can generate correct shape.

You can assume that we have only tree different shapes: Triangle, Square and Rectangle.

Have you met this question in a real interview? Yes
Example
ShapeFactory sf = new ShapeFactory();
Shape shape = sf.getShape("Square");
shape.draw();
>>  ----
>> |    |
>> |    |
>>  ----

shape = sf.getShape("Triangle");
shape.draw();
>>   /\
>>  /  \
>> /____\

shape = sf.getShape("Rectangle");
shape.draw();
>>  ----
>> |    |
>>  ----
"""
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    # Write your code here
    def draw(self):
        print "  /\\"
        print " /  \\"
        print "/____\\"


class Rectangle(Shape):
    # Write your code here
    def draw(self):
        print " ----"
        print "|    |"
        print " ----"


class Square(Shape):
    # Write your code here
    def draw(self):
        print " ----"
        print "|    |"
        print "|    |"
        print " ----"


class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == "Square":
            return Square()
        if shapeType == "Triangle":
            return Triangle()
        if shapeType == "Rectangle":
            return Rectangle()
        return None
