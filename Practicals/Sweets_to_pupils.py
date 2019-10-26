#!/usr/bin/env python3

"""
  Divide sweets per pupils
"""



try:
    number_of_pupils = int (input ('Enter the number of pupils: '))

    if number_of_pupils < 0:
        print ('Error: You must enter a positive number of pupils.')
    else:

        number_of_sweets = int(input('Enter the number of sweets: '))

        if number_of_sweets < 0:
            print('Error: You must enter a positive number of sweets')
        else:

            sweets_per_student  = number_of_sweets // number_of_pupils
            if sweets_per_student == 1:
                print ('Each student will receive ', sweets_per_student, 'sweet.')
            else:
                print ('Each student will receive ', sweets_per_student, 'sweets')


except ValueError:
    print ('Please enter an valid number.')