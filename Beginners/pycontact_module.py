#Define an empty dictionary to store contact information as a global variable
contacts={}

#Define a function 'menu' to welcome the user and provide options on how the phonebook works
def menu():
    #Use a try except block inside the function to take care of possible wrong responses by the user
    #Define a variable 'entry' for user options
    try:
        entry =int(input("""Welcome to Py Contact Book.  
                    >>>Py Contact Book commands are: 1,2,3 or 4 <<<
                    >>>What would you like to do?<<<
                    1. Display Your existing contacts
                    2. Create a New contact
                    3. Check an entry 
                    4. Delete an entry
                    5. Exit
                    Enter (1,2,3,4) or enter [5] to exit:  """))

    #For the except block, use a valueerror exception
    #in the exception block re-define the variable 'entry', letting the users aware of what type of inputs should be in there
    except ValueError:
        entry=int(input('Wrong entry! Enter a number [1-5]'))
    #Include decision making processes using the control flow statements
    #This flow control statement will call other functions defined beneath
    if entry ==1:
        #Function for displaying contact
        DisplayAll()
    elif entry==2:
        #Function for adding contact details
        AddContact()
    elif entry==3:
        #Function for viewing contact
        ViewContact()
    elif entry ==4:
        #Function for deleting contact
        DelContact()
    else:
        #Closing statement
        print('\n\b Thanks for using the Py Contact Book')
 
#Define another function display query with required argument query, as disp(query)
#Set up a decision-making process using control flow statements
#Initiate two new functions 'DisplayAll' and 'Addcontact', to be defined below.
def disp(query):
    #Set up a decision making process using control flow statements
    if query in contacts.keys():
        print(contacts[query])
        dlt=input('Want to delete this contact ?[Y/N]').lower()
        if dlt=='y':
            DelContact()
        else:
            DisplayAll()
    else:
        pi=input('Error 404, contact not found. Want to add this contact? [Y/N]').lower()
        if pi=='y':
            AddContact()
        else:
            pass
#Define a new function 'DisplayAll'
#Include decision making using control statements
#Call the menu function defined earlier at the end of this function
def DisplayAll():
    if len(contacts) >= 1:
        print('your contacts are:\n','+'*30)
        for contact, num in contacts.items():
            print(contact, '-----', num)   
    else:
        print('You have an empty Contact List')
        opt=input('Want to Add contacts? Y/N :')
        if opt.capitalize()=='Y':
            AddContact()
        else:
            pass
    menu()
    
#Define a new function AddContact
#Use the try-except block here too
#Include conditions for decision making
#Call the displayall function
#Call the disp(query) function
def AddContact():
    print('You can add a new entry here')
    name=str(input('Enter Name :').capitalize())
    try:
        num = int(input('Enter Num :'))
    except ValueError:
        input('invalid value entered')
        num = 0
        '''return num'''
    if name not in contacts.keys():
        contacts[name]=num
        print('You have successfully added ', contacts[name], 'to your contacts')
        DisplayAll()
    else:
        print('This Contact already exists in phonebook')
        disp(name)
        
#Define a new function 'ViewContact'
#Using decision making here also
#Call the disp(query) function 
def ViewContact():
    query=input('Enter the name or number you want to view: ')
    if type(query)==str:
        query = query.capitalize()
        disp(query)         
    elif type(query)==int:
        print(contacts.values())
        
#Final function for the module
#Define a function 'DelContact' 
#Initiate a decision making
#Call the 'DisplayAll' function
 def DelContact():
    name=str(input('Enter name of the contact you wish to delete').capitalize())
    confirm = input('Are you sure you wish to delete this contact? Y/N: ')
            #Initiate a decision
    if confirm.upper() == 'Y':
            #If yes, delete contact from Phonebook
                contacts.pop(name)
    else:
        pass
    DisplayAll()
 
