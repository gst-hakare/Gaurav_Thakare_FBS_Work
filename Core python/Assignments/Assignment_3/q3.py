# Q Write a program to input angles of a triangle and check whether triangle is valid or not.

angle_1 = int(input('Enter 1st angle : '))
angle_2 = int(input('Enter 2nd angle : '))
angle_3 = int(input('Enter 3rd angle : '))

if (angle_1 + angle_2 + angle_3 ) == 180:
    print('angles of a triangle is valid')
else:
    print('angles of a triangle is not valid')
