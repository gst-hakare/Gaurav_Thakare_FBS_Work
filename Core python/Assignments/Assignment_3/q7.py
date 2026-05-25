# Q Write a program to check if user has entered correct userid and password.

user_name = 'gaurav1234'
pass_word = 'Gst@1234'

username = input('Enter a username : ')
password = input('Enter a password : ')

if username == user_name and password == pass_word:
    print('Login succesfully')
else:
    print('Invalid username or password')