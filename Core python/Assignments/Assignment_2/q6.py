'''WAP to calculate total salary of employee based on basic, da=10% of basic,
ta=12% of basic, hra=15% of basic.'''

basic_salary = float(input('Enter baseic salary of a employee : '))

total_salary = basic_salary + (basic_salary * 0.1) + (basic_salary * 0.12) + (basic_salary * 0.15)

print(f'Total salary of a employee is {total_salary}.')