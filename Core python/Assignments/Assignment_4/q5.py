# Q WAP to print Fibonacci series upto n.
n = int(input('Enter a number : '))
a = -1
b = 1
# count = 0

# while (count <= n):
#     c = a + b
#     if (c > n):
#         break
#     print(c)
#     a = b
#     b = c
#     count += 1



for i in range(n):
    c = a + b
    if c == n:
        break
    print(c)
    
    a = b
    b = c
