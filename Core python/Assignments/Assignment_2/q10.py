# Q. Write a program to reverse three-digit number.

num = int(input('Enter three digit number : '))

d1 = num % 10
num = num // 10

d2 = num % 10

d3 = num // 10

reverse = d1 * 100 + d2 * 10 + d3

print(f'reverse of three digits is {reverse}.')





