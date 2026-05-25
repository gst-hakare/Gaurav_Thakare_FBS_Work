# Q Input 5 subject marks from user and display grade(eg.First class,Second class ..)

maths = int(input('Enter marks of maths : '))
science = int(input('Enter marks of science : '))
marathi = int(input('Enter marks of marathi : '))
hindi = int(input('Enter marks of hindi : '))
english = int(input('Enter marks of english : '))

total_marks = maths + science + marathi + hindi + english
percentage = total_marks / 5

print(f'Percentage : {percentage}')

if percentage >= 60:
    print('Pass with a first class')
elif percentage >= 45:
    print('Pass with a second class')
elif percentage >= 35:
    print('Pass')
else:
    print('Fail')