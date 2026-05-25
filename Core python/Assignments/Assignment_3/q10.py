# Q wap to check if person is eligible to marry or not (male age >=21 an female age>=18)

gender = input('Enter gender of a person (M/F) : ')
age = int(input('Enter age of a person : '))

if gender == 'M':
    if age >= 21:
        print('Eligible for marriage')
    else:
        print('Beta padhai karo abhi')
else:
    if age >= 18:
        print('Eligible for marriage')
    else:
        print('Bacchi ho tum abhi')