#Q  2. Write a program to calculate area of circle

def area_circle(radius):
    return (3.14 * (radius ** 2))

radius = float(input('Enter radius of a circle : '))
area = area_circle(radius)

print(f'Area of a circle is {area}')