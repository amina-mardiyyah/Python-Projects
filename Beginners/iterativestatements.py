#WHile Loop
list = ['running','sleeping', 'eating']
hobbies = input('Enter a hobby: ')
hobbies = hobbies.lower()
while hobbies in list:
    print('Great choice')
else:
    print('Tell me more')

#For Loop
list = ['running','sleeping', 'eating']
hobbies = input('Enter a hobby: ')
hobbies = hobbies.lower()
for hobbies in list:
    print('Great choice')
else:
    print('Tell me more')
