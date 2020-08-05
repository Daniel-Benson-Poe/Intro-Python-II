from room import Room
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

# Make a new player object that is currently in the 'outside' room.
player = Player("test_dummy", room['outside'])

# create repr that allows user input of the form "n", "s", "e", "w", or "q"
def input_parser():

    print("enter one of the following keys: ")
    command = input("'n' (go north), 's' (go south), 'e' (go east), 'w' (go west), or 'q' (quit game)\n")
    # Convert to lower case in the chance that one of the keys is entered as a capital
    return command.lower() 

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

# Welcome player to the game
print(f"Welcome {player.name} to Adventure Text.")

# Creates infinite loop that only exits when players quits the game
while True:
    print(player.__str__()) # print out player's movement into the current room
    print(player.current_room.__str__())
    # Upon user input, create a loop that checks the user's input
    # Start by checking if input is recognized as an acceptable response - if not, tell the player to try again
    # If the player enters a direction that the current room does not connect to, let player know and have them try again
    command = input_parser()
    if command == 'q':
        exit()
    # Run code within the if conditional that passes: 
    #                               # if n, move player class to the current room's n_to if able
    #                               # if s, move player class to the current room's s_to if able
    #                               # if e, move player class to the current room's e_to if able
    #                               # if w, move player class to the current room's w_to if able
    # player movement north:
    if command == 'n':
        # Checks if current room contains a link to the north

        if player.current_room.n_to:
                player.current_room = player.current_room.n_to # move player to the room to the north
        
        else:
        # If n_to room does not exist in current room, tell the player and have them input a new command.
            print("You have run into a dead end. Try selecting a different direction.")
    
    if command == 's':
        # Checks if current room contains a link to the south

        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to # move player to the room to the south
        
        else:
            # If s_to room does not exist in current room, tell the player and have them input a new command.
            print("You have run into a dead end. Try selecting a different direction.")

    if command == 'e':
        # Checks if current room contains a link to the east

        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to # move player to the room to the east
        
        else:
            # If e_to room does not exist in current room, tell the player and have them input a new command.
            print("You have run into a dead end. Try selecting a different direction.")

    if command == 'w':
        # Checks if current room contains a link to the west

        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to # move player to the room to the west
        
        else:
            # If w_to room does not exist in current room, tell the player and have them input a new command.
            print("You have run into a dead end. Try selecting a different direction.")


# if __name__ == "__main__":
#     # Test that our player class and room class are working correctly
#     print(player.name, player.__str__(), player.current_room)
    