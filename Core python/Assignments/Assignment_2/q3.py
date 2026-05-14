# Convert distant given in feet and inches into meter and centimeter.

feet = int(input('Enter feet : '))
inches = int(input('Enter inches : '))

cent = (feet * 30) + (inches * 2.5)

meter = cent // 100
centimeter = cent % 100

print(f'{feet} feet {inches} inches means {meter} meter {centimeter} centimeter')