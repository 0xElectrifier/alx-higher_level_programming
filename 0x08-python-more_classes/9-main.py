#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
#Rectangle = __import__('9-tes').Rectangle

new = Rectangle(2, 4)

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
