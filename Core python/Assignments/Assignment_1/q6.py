#wap to input two angles from user and find third angle of the triangle.

a = float(input('enter 1st angle of a triangle : '))
b = float(input('enter 2nd angle of a triangle : '))

c = 180 - (a + b)

print(f'Third angle of a traingle is {c} degree.')
