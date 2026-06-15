# Q 9. Write a program to check if entered number is a palindrome or not.

def chk_palindrome(num):
    reverse = 0
    n = num
    while (n > 0):
        d = n % 10
        reverse = reverse * 10 + d
        n = n // 10
    if num == reverse:
        print(f'{num} is palindrome')
    else:
        print(f'{num} is not palindrome')

num = int(input('Enter a number to check palindrome : '))
chk_palindrome(num)