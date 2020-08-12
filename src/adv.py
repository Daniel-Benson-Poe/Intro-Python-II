from room import Room
from player import Player
from items import Item, Weapon
import time
from enemies import Enemy
from battle_sequence import Battle
from locations import *
from game_loop import *
from player_input import *
from dialogue import Dialogue
from chapter_1 import ChapterOne

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player()

# Set up chapter 1
chapter_1 = ChapterOne(player)

while True:
    # set up game loop
    game_loop = GameLoop(player)
    
    if player.last_action == "Used item":
        if player.used_item == "treasure key" and player.current_room.name == "Narrow Passage":
            chapter_1.unlocked_door_in_narrow()
            player.used_item = None
            player.last_action = None
        elif player.used_item == "torch" and player.current_room.name == "Dark Room":
            chapter_1.lit_treasure_room()
            player.used_item = None
            player.last_action = None
