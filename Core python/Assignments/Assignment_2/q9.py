# Q. Write a program to swap two numbers without using third variable.

x = int(input('enter value of x: '))
y = int(input('enter value of y: '))

x,y = y,x

print(f'value of x is {x}.')
print(f'value of y is {y}.')