#Define a function to welcome the user and provide options on how the phonebook works
def welcome():
    #Create an entry variable using the input function and multiple line strings format
    entry = int(input("""Welcome to Py Contact Book.  
                    >>>Py Contact Book commands are: 1,2,3 or 4 <<<
                    >>>What would you like to do?<<<
                    1. Display Your exiting contacts
                    2. Create a New contact
                    3. Check an entry 
                    4. Delete an entry
                    5. Exit
                    Enter your entry here(1,2,3 0r 4):  """))
    
#Close the function    
    return entry

#Define a function Phonebook
def phonebook():
    #initiate an empty contact dictionary to store values
    contact = {}
    
    #initiate a while loop to continuously run the phonebook program
    while True:
        #call welcome function. 
        #Set entry variable to welcome function
        entry = welcome()
        
        #Create conditions for  decision making for any option entered by the user
        if entry == 1:
            #For first entry Check if contact dict is empty
            #If not empty,i.e bool(contact)==False, Print current contact list
            if bool(contact) != False:
                for k, v in contact.items():
                    print(k, '-->', v)
             #Else inform the user that the contact book is empty
            else:
                print('You have an empty phonebook! Go back to the menu to add a new contact')
        #Decision For the 2nd entry
        elif entry == 2:
            #Request for phone number and contact name
            phone_number = input('Please Enter a number: ')
            contact_name = input('What would you like to Save the name as? Enter in the format "FirstName,LastName".: ')
            
            #Check if the contact number already exits in Phonebook
            #If it does not, update current contact list in PhoneBook
            if phone_number not in contact.items():
                contact.update({contact_name:phone_number})
                #Print a success message
                print('Contact successfully saved')
                print('Your updated phonebook is Shown below: ')
                #Loop through Phonebook and display each contact in a separate line
                for k, v in contact.items():
                    print(k, '-->', v)
            #Else display a message to inform the user that contact already exits
            else:
                print('That contact already exits in your Phonebook')
                
        #Create a decision for the third entry
        elif entry == 3:
            #initiate a name variable which user wishes to view
            name = input('Enter the name of the contact details you wish to view: ')
            #Create a condition to check if the entered name is in the phonebook
            if name in contact:
                #If yes, print the required contact
                print('The contact is',name,':',contact[name])
                
                #Else inform the user that the contact does not exist
            else:
                print('That contact does not exist! Return to the main menu to enter the contact')
                
         #Create a decision for entry 4       
        elif entry == 4:
            #Initiate a name variable
            name = input('Enter the name of the contact you wish to delete: ')
            #check if contact exists
             if name in contact:
                #print the required contact
                print('The contact is',name,':',contact[name])
                
                #Else inform the user that the contact does not exist
            else:
                print('That contact does not exist! Return to the main menu to enter the contact')
            
            
            #COnfirm if user wishes to delete contact
            confirm = input('Are you sure you wish to delete this contact? Yes/No: ')
            #Initiate a decision
            if confirm.capitalize() == 'Yes':
                #If yes, delete contact from Phonebook
                contact.pop(name,None)
                #Loop through Phonebook and print updated contact list
                for k, v in contact.items():
                    print('Your Updated Phonebook is shown below:')
                    print(k, '-->', v)
            #ELse return to main menu
            else:
                print('Return to Main Menu')
            #Break program for fifth entry
        elif entry == 5:
            print('Thanks for using the Py Contact Book')
            break
            
        #Error Message    
        else:
            print('Incorrect Entry!')

    
