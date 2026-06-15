# Q 4. WAP to print Armstrong number within a given range
start = int(input('Enter a starting number : '))
end = int(input('Enter a ending number : '))


for i in range(start, end):
    power = len(str(i))
    sum = 0
    num = i
    while num > 0:
        d = num % 10
        sum = sum + (d ** power)
        num = num // 10
    if sum == i:
        print(i, end= ' ')


