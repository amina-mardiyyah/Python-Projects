
#Import the random module
import random

#Create and store greetings and likely responses in a list data structure
greetings = ["hola!I'm Annie", "hello! I'm Annie", 'hi!', 'Hi', 'hey!','hey',"What's up", 'Good day']
responses = ['Okay',"I'm fine","I'm doing great", "I'm ok","I'm good",'Good','Awesome', 'Great','Superb','nice','ok']

#question = ['How are you?','How are you doing?']

# Initiate a Welcome message and an introduction
name = input('Welcome! What is your name?: ')
print('>>>')
print((random.choice(greetings),name,'!Nice to meet you'))

#1st conversation
feelings = input("How are you today?: ")

if feelings.capitalize() in responses:
    print("I'm so Glad to hear that!")
else:
    print('Oh dear!')
    print('Why do you feel', feelings)
    reason = input('Please tell me: ')
    print('I understand.It is absolutely ok to feel that way sometimes.Thanks for sharing')



#2nd Conversation
#Ask for user's age
userAge = int(input('How old are you?: '))
if userAge >= 18 and userAge <= 24:
    print('Cool!You are a Young Adult')
elif userAge >= 25 and userAge <= 44:
    print('Whoa!You are all grown up!')
elif userAge > 45:
    print('Great!You seem like an elderly person')
else:
    print('It feels so nice to be a teenager')

#Conversation about continent
world = ('Africa', 'Antractica','Asia', 'Australia', 'Europe','North-America', 'South-America') 

continent = input('What continent are you from?: ').capitalize()
if continent in world and continent == 'Africa':
          print("That's cool! I have heard a lot about Africa and its richness for culture and nature parks")
          print('I sure would love to visit someday')
elif continent in world and continent == 'Asia':
          print('Nice! Asians have a very unique culture. Beautiful culture, beautiful places, beautiful people.')
elif continent in world and continent == 'Europe':
          print('Amazing!Europe is known for its unique building structures')
elif continent in world and continent == 'Antractica':
          print('I heard the weather tends to get extreme over there and very few people live there. So glad to be chatting with a native')
elif continent in world and continent == 'Australia':
          print('I would definitely love to visit sometime.I have a few friends from over there and they also tell me a lot of interesting stories')
else:
          print('I have been to North-America a couple of times. I also love watching mexican movies. I think America is generally a rich continent')

#Conversation on Year
year = int(input('I am not very good at dates. What year is it?: '))
if year == 2020:
    print('You are very smart! It is the year of the global pandemic')
    print('Do stay safe at all times!')
else:
    print('You are a genius! I have troubles remembering dates')
    
#Ending the conversation
print('I absolutely loved chatting with you today. Hope to talk to you some other time')
print('Bye', name, '!You have quite an interesting personality. Do Take care!')
