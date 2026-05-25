# Q WAP to print all numbers in a range divisible by a given number.
n = int(input('Enter a range : '))

num = int(input('Enter a divisor : '))

for i in range(1,n):
    if (i % num == 0):
        print(i)
    else:
        pass