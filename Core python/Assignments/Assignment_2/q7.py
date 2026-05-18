# Q. Find the sum of three-digit number.

num = int(input('Enter three digit number : '))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num

sum = d1 + d2 + d3

print(f'sum of three digits number is {sum}.')
