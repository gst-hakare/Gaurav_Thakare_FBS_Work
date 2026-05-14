#wap to enter P, T, R and calculate Compound Interest.



p = float(input('enter principle amount : '))
t = float(input('total year : '))
r = float(input('rate of interest : '))


compound_interest = p*((1+(r/100))**t)-p


print(f'{compound_interest} is the compound interest.')