''' Q. Write a program to accept an integer amount from user and tell minimum
number of notes needed for representing that amount.'''

amount = int(input('Enter amount : '))

two_thousand = amount // 2000
amount = amount % 2000

five_hundred = amount // 500
amount = amount % 500

two_hundred = amount // 200
amount = amount % 200

one_hundred = amount // 100
amount = amount % 100

fifty = amount // 50
amount = amount % 50

twenty = amount // 20
amount = amount % 20

ten = amount // 10
amount = amount % 10

print(f'''two_thousand : {two_thousand}
five_hundred : {five_hundred}
two_hundred : {two_hundred}
one_hundred : {one_hundred}
fifty : {fifty}
twenty : {twenty}
ten : {ten}''')