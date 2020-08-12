import time
from dialogue import Dialogue
from room import Room
from player_input import InputParser
from player import Player
from items import Item, Weapon
from enemies import Enemy
from battle_sequence import Battle

class ChapterOne:
    def __init__(self, player):
        self.player = player
         # Declare the items
        self.items = { 
            'torch': Item('Torch',
                        "A small torch used for lighting dark passages."),

            'treasure key': Item("Treasure Key",
                        "A glimmering gold key used to unlock the treasure room."),
            
        }
        # Declare the weapons
        self.weapons = {
            'small dagger' : Weapon("Small Dagger", "Just a basic dagger. Can be used to cause minimal damage. 10-15 dmg dealt.", dmg_range=[10, 15])
        }

        # Declare all the rooms
        self.room = {
            'outside':  Room("Outside Cave Entrance",
                            "North of you, the cave mount beckons"),

            'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east.""",
                        items = {"torch": self.items['torch']}),

            'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""",
                        items = {"treasure key" : self.items['treasure key']}),

            'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
        to north. A locked door blocks your way at the northern end. The smell of gold permeates the air.""",
                        items_useable={"treasure key" : self.items['treasure key'].name}),

            'dark' : Room("Dark Room", """You find yourself surrounded by darkness. You are unable to 
        see any of your surroundings. You can either go back the way you came or figure out 
        how to light your way.""",
                        items_useable={"torch" : self.items['torch'].name}),

            'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by earlier explorers. The only exit is to the south.""",
                        items = {"small dagger" : self.weapons['small dagger']}),
        }


        # Link rooms together

        self.room['outside'].n_to = self.room['foyer']
        self.room['foyer'].s_to = self.room['outside']
        self.room['foyer'].n_to = self.room['overlook']
        self.room['foyer'].e_to = self.room['narrow']
        self.room['overlook'].s_to = self.room['foyer']
        self.room['narrow'].w_to = self.room['foyer']
        self.room['narrow'].n_to = self.room['narrow'] # Default n_to for narrow set to narrow; need key to reset this.
        self.room['dark'].s_to = self.room['narrow']
        self.room['dark'].n_to = self.room['dark'] # Default n_to for dark set to dark; need torch to reset this
        self.room['treasure'].s_to = self.room['narrow']

        # Set player's current location
        self.player.current_room = self.room['outside']

    def unlocked_door_in_narrow(self):
        print("""You withdraw the golden key from your pouch, reach forward to insert 
it into the keyhole before you, and you hear a satisfying 'click' as the door is unlocked.\n""")
        print(f"The {self.player.used_item.title()} has already been used and is now useless. It has been discarded from your inventory.\n")
        self.player.current_room.description = """The narrow passage bends here from west
to north. The smell of gold permeates the air."""
        self.room['narrow'].n_to = self.room['dark']


    def lit_treasure_room(self):
        print("You light the torch, sending a flickering glow about the room you reside in.\n")
        self.player.current_room.n_to = self.room['treasure']
        self.player.current_room = self.player.current_room.n_to
        self.player.current_room.enemy = Enemy("Goblin")
        print(f"The lit {self.items['torch'].name} has been placed upon a holster on the nearby wall. It has been removed from your inventory.\n")
        time.sleep(1)
        self.player.current_room.print_room_details()
        time.sleep(1)
        self.player.current_room.enemy.print_description()
        time.sleep(1)
        battle = Battle(self.player, self.player.current_room.enemy)
        battle.main_battle_loop()
        self.player.current_room.enemy = None
