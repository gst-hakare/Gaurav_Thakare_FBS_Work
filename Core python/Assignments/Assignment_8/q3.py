# a. 1+ 2 + 3 + 4+..... + n

def sumofseries(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
    
n = int(input('Enter number till you want sum of series : '))
res = sumofseries(n)
print(f'Sum of series till {n} is {res}')

# b. 1!+ 2! + 3! + 4!+..... + n!

def fact(n):
    sum = 0
    for i in range(1,n+1):
        product = 1
        for j in range(1,i+1):
            product = product * j
        sum += product
    return sum
n = int(input('Enter number till to find addition of factorials : '))
res = fact(n)
print(f'The addition of factorials till {n} is {res}')


# c. 1^1 + 2^2 + 3^3+ ...... n^n

def power(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i ** i
    return sum

n = 5
res = power(n)
print(res)