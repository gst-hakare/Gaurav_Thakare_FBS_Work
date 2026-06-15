# Q 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

id = 'gaurav@1230'
pass_word = '1234'



count = 0

while count<3:
    user_id = input('enter user id of a user : ')
    password = input('Enter password of user : ')
    if user_id == id and password == pass_word:
        print('Logged in successful')
        break
    else:
        print('Invalid credential')

    count += 1
else:
    print('terminated')


