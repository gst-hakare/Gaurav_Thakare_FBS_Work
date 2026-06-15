# Q 1. Write a program to calculate area of rectangle

def area_rectanle(l,b):
    return (l*b)

l = float(input('Enter length of rectangle : '))
b = float(input('Enter breadth of rectangle : '))
area = area_rectanle(l,b)
print(f'Area of Rectangle is {area}')
