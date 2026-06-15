# Q 6. Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fibonacci(n):
    a = 0
    b = 1
    while (a <= 10):
        print(a, end= ' ')
        c = a + b
        a = b
        b = c
    

n = int(input('Enter numnber : '))
fibonacci(n)


