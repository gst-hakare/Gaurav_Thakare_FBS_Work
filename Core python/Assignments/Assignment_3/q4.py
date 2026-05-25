# Q Wap to input all sides of a triangle and check whether triangle is valid or not.

side_1 = int(input('Enter 1st side of a triangle : '))
side_2 = int(input('Enter 2nd side of a triangle : '))
side_3 = int(input('Enter 3rd side of a triangle : '))

if (side_1 + side_2) > side_3 and (side_2 + side_3 > side_1 and (side_1 + side_3) > 2):
    print('sides of a triangle is valid')
else:
    print('sides of a triangle is not valid')