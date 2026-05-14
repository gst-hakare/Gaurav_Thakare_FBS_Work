# Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

temp_cel = float(input('Enter temperature in celsius : '))

fehrenheit = (9/5)*temp_cel + 32

print(f'{temp_cel} degree celsius means {fehrenheit} fehrenheit.')