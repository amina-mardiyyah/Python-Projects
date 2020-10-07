#import the built-in python modules: Json, urllib and random
import json
import random
import urllib.request

#Define the following variables to request for a random word from the github repository
url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())

#Define a function welcome
def welcome():
    
    #Define a name variable
    name = input("""
                ================================================================
                > Welcome to the Hangman Game! Please Enter your preferred game name:  <
                """).capitalize()
    
    #Use a decision making process to accept only alphabets as name
    if name.isalpha() == True:
        print(""">> Hi!""",name,"""Glad to have you here! <<<
                You will be playing against the computer today.
                The computer will randomly choose a word and you will try to guess what the word is.
                You can always invite your friends for a fun time together
                ==========================================================
                Good Luck! Have fun playing""")
        
           
    else:
        print('Please enter your name using letter only')
        name = input('Enter a game name here:  ')
        print('Hi!',name,'Please go through the rules of the game below')
        

#Define another function play_again
#Add a docstrings
def play_again():
    
    """ This function asks user/player if he/she wishes to replay the hangman game """
    response = input("Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()
    reply = ('y','n')

    
        #Create a decision making process
    if response not in reply:
        print('Invalid Entry! Please check that you entered the correct input: ')
        response = input("Please enter the correct input here. Either yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()
        
    else:
        if response == 'y':
            game_run()
                                        
        elif response == 'n':
            print('Hope you had fun playing the game. See you next time')
        

#Define another function get_word for generating random words for the user to guess.
#Add a docstrings
def get_word():
    """ This function generates the word the user will attempt guessing.
    Using the Json and Urllib library, this word will be randomly generated from the defined link.
    So in a way, this function acts as an Automatic random word generator for the Hangman game"""
    
    return random.choice(words).lower()

#Define another function game_run()
#Add a docstring if desired

def game_run():
    #call the welcome function to get the game running
    welcome()
    
    #Define a variable alpahabet
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    
    #Set guess word to get_word function for a random word to be generated
    word = get_word()
    
    #Initiate an empty list for guessed letter
    letters_guessed = []
    
    #Initiate a tries variable for number of tries by the user
    tries = 7
    
    #Set inital guess to false
    guessed = False
    
    #Print an empty line
    print()
    
    #Print a guess hint for the user for number of letters contained in the word

    print('The word contains', len(word), 'letters.')
    print(len(word) * '_')
    
    #Initate a while loop and create decisions, taking into consideration if the user decides to enter just a single letter or  the full word
    #Also a create decisions for if user inputs a wrong entry and if user inputs letters and it is not equal to the total number of letters in the word to guess
    #Deduct tries each user fails to guess incorrectly
    while not guessed and tries > 0:
        print('You have ' + str(tries) + ' tries')
        guess = input('Guess a letter in the word or enter the full word.').lower()
        #user inputs a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print('You are yet to enter a letter. Check your entry, make sure you enter an alphabet not a number')
            elif guess in letters_guessed:
                print('You have already guessed that letter before.Try again!')
            elif guess not in word:
                print('Sorry, that letter is not part of the word.')
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print('Great! That letter exists in the word!Keep Going!!')
                letters_guessed.append(guess)
            else:
                print('Check your entry!You might have entered the wrong entry')

        #user inputs the full word
        elif len(guess) == len(word):
            if guess == word:
                print('Great Job! You guessed the word correctly!')
                print(The word is': word)
                guessed = True
            else:
                print('Sorry, that\'s not the word!')
                print('The correct word was: ', word)
                tries -= 1

        #user inputs letters and it is not equal to the total number of letters in the word to guess.  
        else:
            print('The length of your guess is not the same as the length of the correct word.')
            tries -=1

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '_'
            #Initiate the display hangman image here
            #The function for is defined below
            print(hangman(tries))
            print(status)
           

        if status == word:
            print('Great Job! You guessed the word correctly!')
            guessed = True
        elif tries == 0:
            print("Opps! You ran out of guesses and you couldn't guessed the word.")
            print('The correct word was: ', word)

    #Initiate play_again function if user wishes to continue
    play_again()
                      

#Define a new function for the hangman image
#Use the list Data structure and intuitively draw the hangman image. 
#Use indexing and multiple line string format to draw image progression at each position such that the images will be displayed accordingly for a given number of tries left
                      
def hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]
#Full program run
game_run()
