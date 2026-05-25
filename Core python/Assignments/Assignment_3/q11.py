''' Q Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''

a = int(input('Enter age of a person : '))
b = int(input('Enter age of a person : '))
c = int(input('Enter age of a person : '))
d = int(input('Enter age of a person : '))
e = int(input('Enter age of a person : '))

amount = int(input('Enter ticket amount of person : '))
total_amount = 0 

if a < 12:
    total_amount = total_amount + (amount - (amount * 0.3))
elif a > 59:
    total_amount = total_amount + (amount - (amount * 0.5))
else:
    total_amount = total_amount + amount

if b < 12:
    total_amount = total_amount + (amount - (amount * 0.3))
elif b > 59:
    total_amount = total_amount + (amount - (amount * 0.5))
else:
    total_amount = total_amount + amount

if c < 12:
    total_amount = total_amount + (amount - (amount * 0.3))
elif c > 59:
    total_amount = total_amount + (amount - (amount * 0.5))
else:
    total_amount = total_amount + amount

if d < 12:
    total_amount = total_amount + (amount - (amount * 0.3))
elif d > 59:
    total_amount = total_amount + (amount - (amount * 0.5))
else:
    total_amount = total_amount + amount

if e < 12:
    total_amount = total_amount + (amount - (amount * 0.3))
elif e > 59:
    total_amount = total_amount + (amount - (amount * 0.5))
else:
    total_amount = total_amount + amount

print(f'Total amount is {total_amount}.')

