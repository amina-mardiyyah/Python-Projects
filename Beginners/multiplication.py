##Define a variable num, using the int and input function
##num = int(input('Which number would you like to use for your multiplication table: '))
##
##Create an iterative condition using the for loop and the range function
##Set a start point at 1 and end point at 13
##This is so that the multiplication table runs and stops at 12
##
##for i in range(num):
##    for j in range(i):
##        print(num*i, end="")
##    print("\r")

#Creating a pattern in Python with a nested loop
for pattern in range(1,10):
    for stars in range(pattern):
        print('*',end="")
    print("")
