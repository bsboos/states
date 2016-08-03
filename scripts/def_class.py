#!/usr/bin/env python

# views.py
def basic_addition(num1, num2):

	the_sum  = num1 + num2
	print the_sum
	return the_sum


def basic_subtraction(num1,num2):
	the_sum = num1- num2
	print the_sum
	return the_sum

#urls.py
basic_addition(5,5)
basic_subtraction(17,10)

#model.py
class Shape:
	area = 25;

#import_stuff.py 

new_rect = Rectangle()

print new_rect.area() 


# class Rectangle(Shape):
# 	sides = 5 
# 	width = 7 
# 	hight = 7 


# new_shape = Shape()

# print new_shape.area 
# new_rect = Rectangle() 


# print new_rect.sides
# print new_rect.hight
# print new_rect.width
# print new_rect.area 