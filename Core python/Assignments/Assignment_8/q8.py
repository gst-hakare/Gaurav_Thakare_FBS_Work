# Q 8. Write a program find reverse of a number

def reverse_number(n):
    num = n
    reverse = 0
    while num > 0:
        d = num % 10
        reverse = reverse * 10 + d
        num = num // 10
    return reverse

n = int(input('Enter number to reverse it : '))
res = reverse_number(n)

print(f'reverse of {n} is {res}')


