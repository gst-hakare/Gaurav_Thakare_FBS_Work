# Q WAP to print factorial of a number .

n = int(input('Enter a number to find its factorial : '))
fact = 1
for i in range(n,0,-1):
    fact *= i

print(fact)
