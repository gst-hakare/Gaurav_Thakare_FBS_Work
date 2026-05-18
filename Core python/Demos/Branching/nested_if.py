# nested if

gender = input('Enter gender (m/f) : ')
age = int(input('Enter age : '))

if gender == 'm':
    if age >= 21:
        print('eligible for marriage')
    else:
        print('Bete padhai karle pehle.')
else:
    if age >= 18:
        print('eligible for marriage')
    else:
        print('Bacchi hai tu abhi.')


        
    
   