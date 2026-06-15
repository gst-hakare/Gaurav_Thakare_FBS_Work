# Q 4. Sum of all odd numbers between 1 to n

def odd(n):
    sum = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            sum = sum + i
    return sum
n = int(input('Enter number till you want odd numbers : '))

res = odd(n)
print(f'Sum of 1 to {n} odd numbers is {res}')
    
