# Q 5. Sum of all prime numbers between 1 to n

def prime(n):
    sum = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            sum += i
    return sum

n = int(input('Enter number till you want sum of prime numbers : '))

res = prime(n)
print(f'Sum of all prime numbers from 1 to {n} is {res}')


# def prime(n):
#     sum = 0
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         sum = sum + n
#     return sum

# n = int(input('Enter number you want add of prime numbers : '))
# res = prime(n)
# print(f'Sum of all prime numbers from 1 to {n} is {res}')
