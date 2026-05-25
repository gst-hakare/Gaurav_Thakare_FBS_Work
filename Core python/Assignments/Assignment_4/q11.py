# Q WAP to check if given number Strong Number.

num = int(input('Enter a number : '))
n = num
sum = 0
while (n > 0):
    d = n % 10
    fact = 1
    for i in range(d,0,-1):
        fact *= i 
    sum += fact
    n = n // 10
if sum == num:
    print('strong number')
else:
    print('not strong number')
