# Q Write a program to calculate profit or loss.

cost_price = int(input('Enter a cost price : '))
selling_price = int(input('Enter a selling price : '))


loss = cost_price - selling_price
profit = selling_price - cost_price

if cost_price > selling_price:
    print(f'loss = {loss}')
else:
    print(f'profit = {profit}')