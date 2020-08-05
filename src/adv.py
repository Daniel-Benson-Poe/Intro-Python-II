from room import Room, Outside, Foyer, Overlook, Narrow, Treasure
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# TODO: Make a new player object that is currently in the 'outside' room.
# player = Player(name, Outside())  # default parameters should be passed into this original player call.

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

# TODO: create repr that allows user input of the form "n", "s", "e", "w", or "q"
# Along the lines of: input("enter one of the following keys: 'n' (go north), 's' (go south), 'e' (go east), 'w' (go west), 'q' (quit game)")
# Upon user input, create a loop that checks the user's input
# Start by checking if input is recognized as an acceptable response - if not, tell the player to try again
# If the player enters a direction that the current room does not connect to, let player know and have them try again
# Run code within the if conditional that passes: 
#                               # if n, move player class to the current room's n_to if able
#                               # if s, move player class to the current room's s_to if able
#                               # if e, move player class to the current room's e_to if able
#                               # if w, move player class to the current room's w_to if able

# TODO: create loop that prints out player's current room, a description of the room, and waits for player to input a cardinal direction
# print player.current_room.__str__  # This will print out string that includes current room name and current room description - built in to Room class
# run repr function created earlier - wait for user response
# repeat the above steps 
# This loop should be controlled by a while_game_running boolean; True until player inputs 'q' to quit the game
# entering 'q' will trigger the while_game_running boolean to switch from True to False, exiting the loop
# Include text that thanks the player for playing?