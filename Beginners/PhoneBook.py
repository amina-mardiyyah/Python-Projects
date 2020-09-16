def welcome():
    entry = int(input("""Welcome to Py Contact Book.  
                    >>>Py Contact Book commands are: 1,2,3 or 4 <<<
                    >>>What would you like to do?<<<
                    1. Display Your exiting contacts
                    2. Create a New contact
                    3. Check an entry 
                    4. Delete an entry
                    5. Exit
                    Enter your entry here(1,2,3 0r 4):  """))
    
    return entry

def phonebook():
    contact = {}
    while True:
        entry = welcome()
        if entry == 1:
            if bool(contact) != False:
                print(contact)
            else:
                print('You have an empty phonebook! Go back to the menu to add a new contact')
        elif entry == 2:
            phone_number = input('Please Enter a number: ')
            contact_name = input('What would you like to Save the name as? Enter in the format "FirstName,LastName".: ')
            if phone_number not in contact:
                contact.update({contact_name:phone_number})
                print('Contact successfully saved')
                print('Your updated phonebook is : ',contact)
            else:
                print('Contact already exits. Would you rather like to update the contact?')
    
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
                print('Updated contact list is: ',contact)
            else:
                print('Return to Main Menu')
        elif entry == 5:
            break
            print('Thanks for using the Py Contact Book')

    
