# JTRPG by JJ Codes
rooms = ({
    'name': 'Reception',
    'item': 'mobile phone'
}, {
    'name': 'Hall'
}, {
    'name': 'Lounge',
    'item': 'sim card'
})
backpack = []
current_location = 0


def look():
    if 'item' in rooms[current_location]:
        print('You are able to see a ' + rooms[current_location]['item'])
    else:
        print('You can\'t see anything in particular.')


def grab():
    if 'item' in rooms[current_location]:
        backpack.append(rooms[current_location]['item'])
        print('You got the ' + rooms[current_location]['item'])
        del rooms[current_location]['item']
    else:
        print('You can\'t grab anything here.')


def inventory():
    print(backpack)

def move_north():
	pass

def move_south():
	pass

#Start
name = input('Welcome to the world of Jeteropaga!\n\nThis is a text-only roleplaying game where you can explore the vast world around you through only text! Shall we start?\nWhat\'s your name?\n')
print('Hi! These are the commands for you to play, ' + name + ':\nL = Look\nG = Grab\nI = Inventory\nN = Travel northward\nS = Travel southward\nQ = Leave (the game)')

#Loop
while True:
    print('\nYou are in the', rooms[current_location]['name'])
    command = input('What do you want to do?\n')
    if command == 'L':
        look()
    elif command == 'G':
        grab()
    elif command == 'I':
        inventory()
    elif command == 'Q':
        break
		else:
				print('\nPlease enter one of the commands.')
#End
print('Thank you so much for playing my game, ' + name + '! I really do hope you enjoyed it.\nI\'m a coder who has only recently started and this will be my 5th day of coding.\nIf there are any bugs or if you have suggestions to improve the game please email: jeromejijo@outlook.com. (Spam will not be tolerated and will be reported immediately.)')
