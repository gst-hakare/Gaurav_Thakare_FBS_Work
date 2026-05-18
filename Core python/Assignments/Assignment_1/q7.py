# Q. wap to Find the Roots of a Quadratic Equation

a = int(input('enter value of a : '))
b = int(input('enter value of b : '))
c = int(input('enter value of c : '))

d = (b**2) - (4*a*c)

r1 = ((-b) + (d**0.5))/(2*a)
r2 = ((-b) - (d**0.5))/(2*a)

print(f'{r1} and {r2} are the roots of quadratic equation.')

