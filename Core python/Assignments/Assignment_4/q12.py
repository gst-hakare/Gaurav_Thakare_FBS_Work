'''Q 12. Write a program to check if given number is Armstrong number or not.
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
4*4*4*4)'''

num = int(input('enter a number to check armstrong : '))
n = num
power = len(str(num))
arm = 0

while(n > 0):
    d = n % 10
    arm = arm + d ** power
    n = n // 10

if arm == num:
    print(f'{num} is an armstrong number')
else:
    print(f'{num} is not an armstrong number')


