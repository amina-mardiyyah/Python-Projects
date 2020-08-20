#Create a welcome message
print("Bonjour! Welcome to Chloe's Chocolate Shop!")

#Ask User for Name and Print a message
name = input('What is your name?: ')
print("Hi " + name + "! What would you like to eat Order?")
print('We have some very tasty and irresistible Chocolates.Take a look at our menu below and make your order')

#Print an empty line
print()
print('For each item, we have the price and the quantity in stock attached')

#Create a Menu using dictionary
menu = {1: ('Caramel Chocolate -> Qty:50', 999.99),
        2: ('Dark Chocolate with Hazelnut -> Qty:120', 1299.99),
        3: ('KitKat Medium Size -> Qty:80',399.99),
        4: ('Toberone White Chocolate(Large)-> Qty:150',1499.99),
        5: 'Option not listed'}

#Iterate through the menu dictionary to show each item, the price and the quantity
for k, v in menu.items():
     print (k, '-->', v)

#print an empty line
print()

#Create an empty list for shopping cart
shopping_cart = []

#Initiate order
items = ("""
Keynames for Shopping
Caramel
Dark Chocolate
Kitkat
Toberone
""")
print(items)
print()
order = input('To make an order, enter the name of the Item using the keyname as listed above:  ')

#Initiate While loop to check if order in listed item
while order.capitalize() in items:
    #append order to empty shopping cart list
    shopping_cart.append(order)
    #Ask user if they wish to add more items
    cart = input('Want to add more items to your basket?Enter Y/N: ')
    #Initiate a while loop to validate user's response
    while cart.lower() == 'y':
        order = input('Enter the name of the item using the keyname: ')
        shopping_cart.append(order)
        cart = input('Want to add more items to your basket?Enter Y/N: ')
    #Close shopping with an else statement
    else:
        print('We organized your shopping list for you, Just in order as you selected the items.View below before proceeding to payment')
        print(shopping_cart)
        print("You'll be redirected to a payment site soon......")
        print('Thank you for shopping with us ',name,' We look forward to seeing you again')
    break #break loop to exit
