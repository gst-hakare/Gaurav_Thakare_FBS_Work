#Wap to calculate the percentage of student based on marks of any 5 subjects

maths = int(input('Enter marks of maths : '))
science = int(input('Enter marks of science : '))
marathi = int(input('Enter marks of marathi : '))
hindi = int(input('Enter marks of hindi : '))
english = int(input('Enter marks of english : '))


total_marks = maths + science + marathi + hindi + english

percentage = total_marks / 5



print(f'percentage of student based on marks of any 5 subjects is {percentage} %.')

