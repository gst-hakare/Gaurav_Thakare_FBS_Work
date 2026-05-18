num = int(input('Enter a number : '))

if num > 0:
    if num > 50:
        if num > 100:
            if num > 200:
                print(f'{num} is greater than 200.')
            else:
                print(f'{num} is between 101 to 200.')   
        else:
            print(f'{num} is between 51 to 100.')        
    else:
        print(f'{num} is between 0 to 50.')           
else:
    print(f'{num} is less than 0.')