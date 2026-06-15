# Q 7. Write a program to find sum of digits of a number.

def sum_digits(n):
    sum = 0
    num = n
    while num > 0:
        d = num % 10
        sum += d

        num = num // 10
    return sum
    
n = int(input('Enter number to finde sum of : '))
res = sum_digits(n)

print(f'sum of {n} digits is {res}')



