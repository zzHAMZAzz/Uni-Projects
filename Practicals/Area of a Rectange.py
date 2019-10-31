#!/usr/bin/env python3

"""
  Calculate the area of a rectange with given side measurements

"""


try:
    x_measurement = int (input ('Enter side X of the rectangle in CM: '))

    if x_measurement < 0:
        print ('Error: You must enter a positive measurement for side X.')
    else:
        y_measurement = int(input('Enter side Y of the rectangle in CM: '))

        area_of_rectangle = x_measurement * y_measurement

        print("The area of the rectangle is: " + area_of_rectangle.__str__() + "cm²")



except ValueError:
    print ('Please enter an valid number without any letters.')