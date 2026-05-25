''' Q Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)'''

import random

id = 'gaurav@1230'
pass_word = '1234'

user_id = input('enter user id of a user : ')
password = input('Enter password of user : ')

if user_id == id and password == pass_word:
    number = random.randint(1000,9999)
    print(f'enter captcha : {number}')
    captcha = int(input('Enter the captcha : '))
    if captcha == number :
        print('Logged in successful')
    else:
        print('invalid captcha')
else:
    print('invalid credential')

