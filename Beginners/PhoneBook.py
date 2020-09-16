#Define a function for to welcome the user and provide options on how the phonebook works
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

#Define a Phonebook
def phonebook():
    #initiate an empty contact dictionary to store values
    contact = {}
    
    #initiate a while loop
    while True:
        #Set entry to welcome function
        entry = welcome()
        
        #Create conditions decision making
        if entry == 1:
            #Check if contact dict is empty
            #If not empty,i.e bool(contact)==False, Print current contact list
            if bool(contact) != False:
                for k, v in contact.items():
                    print(k, '-->', v)
             #Else inform user that the contact book is empty
            else:
                print('You have an empty phonebook! Go back to the menu to add a new contact')
        elif entry == 2:
            phone_number = input('Please Enter a number: ')
            contact_name = input('What would you like to Save the name as? Enter in the format "FirstName,LastName".: ')
            if phone_number not in contact:
                contact.update({contact_name:phone_number})
                print('Contact successfully saved')
                print('Your updated phonebook is Shown below: ')
                for k, v in contact.items():
                    print(k, '-->', v)
        elif entry == 3:
            name = input('Enter the name of the contact details you wish to view: ')
            if name in contact:
                print('The contact is',name,':',contact[name])
            else:
                print('That contact does not exist! Return to the main menu to enter the contact')
        elif entry == 4:
            name = input('Enter the name of the contact you wish to delete: ')
            print('The contact is',name,':',contact[name])
            confirm = input('Are you sure you wish to delete this contact? Yes/No: ')
            if confirm.capitalize() == 'Yes':
                contact.pop(name)
                for k, v in contact.items():
                    print('The Updated contact list is shown below:')
                    print(k, '-->', v)
            else:
                print('Return to Main Menu')
        elif entry == 5:
            print('Thanks for using the Py Contact Book')
            break
            
            
        else:
            print('Incorrect Entry!')

    
