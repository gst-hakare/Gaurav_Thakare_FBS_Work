# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.




cost_of_ticket = int(input('Enter cost of ticket : '))


total_amount = 0

passenger = int(input('enter passengers count : '))
for i in range(passenger):
    age = int(input('Enter age of person : '))
    if age < 12:
        total_amount = total_amount + (cost_of_ticket - (cost_of_ticket * 0.3))
    elif age > 59:
        total_amount = total_amount + (cost_of_ticket - (cost_of_ticket * 0.5))
    else:
        total_amount = total_amount + cost_of_ticket
print(total_amount)

    
    