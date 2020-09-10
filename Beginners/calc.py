#A simple Calculator

#import the mod module using any alias of choice
import mod as mod

# Define a function for running the calculator

def calc_run():
        # Define variables for two numbers using the int and input function
        num1 = int(input('Please enter a number: '))
        num2 = int(input('Please enter another number: '))
        #Define a variable for choosing operator
        #Use multi-line text format
        operator = input("""What type of mathematical operation would you like to carry out?
                        Select an option by entering the corresponding number for the desired operation.
                     1. Addition
                     2. Subtraction
                     3. Multiplication
                     4. Division?:
                     Ans:  """)
        #Use conditional statements for decision making
        #Call out each operator from the module using the dot method
                         
        if operator == '1':
                return mod.add(num1,num2)
        elif operator == '2':
                return mod.sub(num1,num2)
        elif operator == '3':
                return mod.mult(num1,num2)
        elif operator == '4':
                return mod.div(num1,num2)
        else:
                return "Wrong input! Kindly enter the correct option"





  
