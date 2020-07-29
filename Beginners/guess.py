#Building a Guessing Game

#create a secret word
secret_word = "Python"

#Create a Guess variable using the input statement

guess = input('Guess what the Secret Word is: ')

#Create a condition using the While keyword

while guess != secret_word:
    print('Oops!Wrong guess.Try again')
    guess = input('Try a new Guess!: ')
print('Yaay! You guessed right.Great job')
##guess = ""
##guess_count = 0
##guess_limit = 3
##out_of_guesses = False
##
##while guess != secret_word and not(out_of_guesses):
##     if guess_count < guess_limit:
##          guess = input("Enter a guess: ")
##          guess_count += 1
##     else:
##          out_of_guesses = True
##
##if out_of_guesses:
##     print("You Lose!")
##else:
##     print("You Win!")
