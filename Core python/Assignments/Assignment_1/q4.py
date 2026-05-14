#wap to enter P, T, R and calculate simple Interest.

p = float(input('enter principle amount : '))
t = float(input('total year : '))
r = float(input('rate of interest : '))

simple_interest = (p*r*t)/100

print(f'{simple_interest} is the simple interest.')