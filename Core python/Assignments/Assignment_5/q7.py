# 7. Write a program to solve the following series :
#   a. 1! + 2! + 3! + 4! + .....n!
#   b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#   c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#   d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#   e. x - x2/3 + x3/5 - x4/7 + .... to n terms



# a. 1! + 2! + 3! + 4! + .....n!

# n = int(input('Enter a  umber : '))
# total = 0

# for i in range(1,n+1):
#     fact = 1
#     for j in range(1,i+1):
#         fact = fact * j

# total = total + fact
# print(total)




#   b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

# n = int(input('Enter a number : '))
# total = 0

# for i in range(1,n+1):
#     total = total + (n ** i)

# print(total)




#   c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input('Enter number : '))

total = 0

for i in range(n):
    total = total + (2 ** i)

print(total)
    



#   d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

# a = int(input('Enter a : '))
# total = 0

# for i in range(1,11):
#     total = total + (a**i)/i


# print(total)


