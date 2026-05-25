# Q wap to check whether the triangle is equilateral, isosceles or scalene triangle.

side_1 = int(input('Enetr a 1st side of a triangle : '))
side_2 = int(input('Enetr a 2nd side of a triangle : '))
side_3 = int(input('Enetr a 3rd side of a triangle : '))

if side_1 == side_2 == side_3:
    print('the triangle is equilateral')
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    print('the triangle is isosceles')
else:
    print('the triangle is scalene')