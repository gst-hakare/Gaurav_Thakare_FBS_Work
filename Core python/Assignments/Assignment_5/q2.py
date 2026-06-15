'''2. Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.'''

n = int(input('Enter no of students : '))
add = 0
count = 0
while count < n:
    sum = 0 
    for i in range(5):
        marks = int(input('Enter marks : '))
        sum += marks
    percentage = sum / 5
    print(percentage)
    add += percentage
    if count < (n-1):
        print('Enter marks of next student')
    count += 1
average = add / n
print(average)

    
    
        
