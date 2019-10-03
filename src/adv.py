from room import Room
from item import Item
import textwrap
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'outside':[Item('shovel',"A need to dig away the burrow"), Item('axe','A part needs to be broken')],
    'foyer':[Item('torch',"Into the dark, yea needs the light"), Item('mask','A need to protect your nose')],
    'overlook':[Item('rope','The mountains has no stairways'), Item('hook','Hook before you leap')],
    'narrow':[Item('expander','Just a little space more for you to pass'),Item('sledge', "In case it can't be expanded it can be broken")],
    'treasure':[Item('map','Your here but to get it you need a map'), Item('shovel','Clear away the dirt')]
}

# Link rooms together
room['outside'].items = item['outside']
room['foyer'].items = item['foyer']
room['overlook'].items= item['overlook']
room['narrow'].items= item['narrow']
room['treasure'].items=item['treasure']




room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Welcome to Adventure Game.\nStart by Inputting your name:')
name = input()
if(name):
    player = Player(name, room['outside'])

# Write a loop that:
    while True:
        print(f'Welcome {name} to the {player.current_room.name} room')
    # * Prints the current room name
        print(f'{player.current_room.description},\nItems:')
        player.current_room.printItems()

        print('Enter Direction(n, w , s , e):')
        x = input()
        # xdir = x +'_to'
        # if(hasattr(player.current_room, xdir) != None):
        #     xvalue = player.current_room.
        if(x == 'n'):
            xvalue = player.current_room.n_to
        elif(x == 's'):
            xvalue = player.current_room.s_to
        elif(x == 'w'):
            xvalue = player.current_room.w_to
        elif(x == 'e'):
            xvalue = player.current_room.e_to
        elif(x == 'q'):
            print(f'Goodbye {name}')
            break
        else:
            print('Invalid direction')
            continue
            # If the user enters a cardinal direction, attempt to move to the room there.
        if(xvalue != None):
            player.current_room = xvalue
            continue
        else:
            print('You are not allowed')
            
    # * Prints the current description (the textwrap module might be useful here).

    # * Waits for user input and decides what to do.
    #

else:
    print('You have not entered your name')
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
