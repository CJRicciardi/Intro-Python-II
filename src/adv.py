from room import Room
# from code import InteractiveConsole
from player import Player
from item import Item
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# functoin for changing location

def try_direction(player, command):
    # attribute will be formatted to change rooms per above linked rooms
    attribute = command + '_to'
# if statement to either change rooms or be informed of players invalid entry
    if hasattr(player.location, attribute):
        player.location = getattr(player.location, attribute)
    else:
        print("\n You cannot go that way!")

# add gold to the treasure room

room['treasure'].items = 'gold'
room['outside'].items = 'wand'

welcome = input("\nWould you like to play the game? (yes/no)").lower().strip()

if welcome == 'yes':
    print("""
    Welcome to our RPG game!
    Your task is to find the hidden treasure.
    You can move in the four cardinal directions, North, East, South, and West.  To move in a direction, input the first leter of the direction you want to go. 'n' for north, 'e' for east etc.  If you would like to quit, at any time make your move 'q'
    Good luck!""" )
    name = str(input("\n What is your player name?"))
elif welcome == 'no':
    sys.exit("You've opened the wrong file.  Better luck next time.")
else:
    print("You've entered an invalid command please input 'yes' or 'no'.")
    welcome = input("Would you like to play the game? (yes/no)").lower().strip()

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# create the REPL for the game


while True:
    print('\n', player.location)
    move = input(f"\n {name}, what's your move?").strip().lower()
    letter = move[0]
    if letter == 'n':
        try_direction(player, letter)
    elif letter == 'e':
        try_direction(player, letter)
    elif letter == 's':
        try_direction(player, letter)
    elif letter == 'w':
        try_direction(player, letter)
    elif letter == 'q':
        sys.exit("Thank you for playing. Better luck next time.")
    elif letter == 'l':
        print(f'\n This room has: {player.location.items}.')
    elif letter == 'a':
        print(f'\n {name} has acquired {player.location.items}.')
        player.items = player.location.items
        player.location.items = []
    elif letter not in ['n', 'e', 's', 'w', 'q', 'l']:
        print('\nThat is an invalid move, try again.')
        print('\n', player.location)    
        move = input(f"\n {name}, what's your move?").strip().lower()




