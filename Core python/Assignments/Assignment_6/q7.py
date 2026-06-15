# g)

for i in range(1,6):
    num = 65
    for j in range(1, 6-i):
        print(' ', end=' ')
    for j in range(1, i+1):
        print(chr(num), end= ' ')
        num += 1
    for j in range(1,i):
        print(chr(num), end= ' ')
        num += 1
    print()
    