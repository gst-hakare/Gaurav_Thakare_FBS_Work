# Q. Write a program to swap two numbers using third variable.

x = int(input('enter value for x: '))
y = int(input('enter value for y: '))

z = y
y = x
x = z

print(f'value of x is {x}.')
print(f'value of y is {y}.')