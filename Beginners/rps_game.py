#import the random module
import random

#Initiate a welcome message

print(""">>> Welcome to the 'Rock,Paper, Scissors game'.Glad to have you here! <<<
        You will be playing against the computer today.
        You can always invite your friends for a fun time together""")

#Create a name variable for the player/user
name = input('Please enter your prefered game name: ')

#print a greeting message for the user/player with game instruction

print('Hi,',name,'! Make a choice below to start the game')

#Create a choice variable using the Tuple data structure

choices = ('Rock', 'Paper', 'Scissors')

#Initiate game sequence using the Flow control statements for decision making
#Start with a while loop
while True:
    #Create a player variable, for player's choice
    player = input("What's your choice? Rock, Paper or Scissors: ").capitalize()
    
    #Check for correct entry
    if player not in choices:
        print('Oops!Wrong Entry.Check Your Spelling')    
    else:
        print(name, "-You picked-->", player)

    #Initiate computer's choice
        computer = random.choice(choices)

    #Print Computer's choice
        print("The Computer's Choice is:",computer)

    #Create game decisions using conditional statements

        if player == computer:
            print("Opps!It's a Tie!Try again!")
        elif (player == 'Rock' and computer == 'Paper') or (player == 'Paper' and computer == 'Scissors') or (player == 'Scissors' and computer == 'Rock'):
            print(name,"Sorry You lose!As per the rules of the game", computer, 'beats', player)
        else:
            print("Yaay!",name, "wins!",player, "beats", computer)
    
        
