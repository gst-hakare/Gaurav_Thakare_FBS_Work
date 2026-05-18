# Q. WAP to calculate selling price of book based on cost price and discount.

cost = float(input('Enter cost price of book : '))
discount = int(input('Enter discount percent on book price : '))

sell_price = cost - (cost * (discount/100))

print(f'selling price of book is {sell_price}.')

