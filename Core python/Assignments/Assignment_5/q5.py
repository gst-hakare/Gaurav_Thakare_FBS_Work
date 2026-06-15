# Q Write a program to print prime numbers between 1 to 100
a = int(input('Enter number where you want prime number from : '))
b = int(input('Enter number till you want prime number : '))
if a > 1:
    for i in range(a,b):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
else:
    pass


        
    