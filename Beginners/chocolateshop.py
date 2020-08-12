#Create a welcome message
print("Hi there, Welcome to Chloe's Chocolate Shop!")

#Ask User for Name and Print a message
name = input('What is your name?: ')
print("Hi " + name + "! What would you like to eat Order?")
print('We have some very tasty and irresistible Chocolates.Take a look at our menu below and make your order')

#Create a Menu
menu = input("\n(a) Caramel Chocolate - NGN999.99 \n(b) Dark Chocolate with Hazelnut - NGN1299.99 \n(c) KitKat Medium Size- NGN399.99 \n(d) Toberone White Chocolate(Large)- NGN1499.99 \n(e) I can't find my Favorite Chocolate: ")

#Add a note

note1 = ("\n Thank you for Shopping with us Today. We hope you love your order.Your order is being processed........")
note2 = ("\n You'll be redirected to a payment site soon......")

#Create Conditionals
if(menu.lower() == 'a'):
    print('Great Choice!!',note1 ,note2, sep='\n')
elif(menu.lower() == 'b'):
    print('You Have such great Taste!!', note1, note2, sep='\n')
elif(menu.lower() == 'c'):
    print('Delicious!!', note1, note2,sep='\n')
elif(menu.lower() =='d'):
    print('Hmmm!Yummy!', note1, note2,sep='\n')
else:
    print("Can't see your Favorite Chocolate? No Worries!!contact us now through our live chat, We've got you covered")

#Final Goodbye message
print('Goodbye! We hope to see you again')
