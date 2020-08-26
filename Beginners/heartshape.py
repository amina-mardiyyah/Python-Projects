#Printing Heart shape
#Ist for loop with 6 rows
for i in range(6):
    #2nd for loop for columns
    for j in range(7):
        #initate if condition using logical and, or, to define where stars will be printed
        if(i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print("*", end="")
        #initiate else statement
        else:
            print(end=" ")
    print()
