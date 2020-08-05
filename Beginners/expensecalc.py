
# A simple Expense Calculator
weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend = ['Saturday', 'Sunday']
day = input('What day is it today? ')
bank_balance = int(input("What's your account balance: "))
if(day in weekend) and (bank_balance > 20000):
    print("Go for shopping")
elif(day in weekday) or (bank_balance < 20000):
    print("You can't go shopping yet")
else:
    print("it's a working day")
