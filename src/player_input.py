from player import Player
from room import Room
from items import Item
import time

class InputParser:
    def __init__(self, player):
        self.movement = None  # holds player movement direction
        self.command = input("What would you like to do? Type 'help' to see a list of options.\n").lower()  # holds player's action
        self.retrieved_item = None  # holds player's last retrieved item
        self.player = player  # holds player class

    def use_player_input(self):

        if 'move' in self.command:
            self.movement_parser()
            
        elif 'get' in self.command:
            self.get_item_parser()

        elif 'help' in self.command:
            self.help()

        elif 'check' in self.command and 'inventory' in self.command:
            self.check_inventory()

        elif 'check' in self.command and 'room' in self.command:
            self.check_room_items()

        elif 'check' in self.command:
            print("What would you like to check?")
            print("Type in 'check' followed by what you would like to check\n")
            print("such as 'room' or 'inventory'.")
            self.command = input()
            self.use_player_input()

        elif 'use' in self.command:
            self.use_item()

        elif 'quit' in self.command:
            self.quit_game()

    def help(self):
        print("Begin your actions with verbs.\n")
        print("Inputs such as 'get item', 'move north', 'check inventory', 'use item', etc.\n")
        print("After specifying movement, directional words are important. Use 'north', 'south', 'east', and 'west' to specify direction.\n")
        print("After typing 'get item', if there are any items in the room you will be given a list of items to choose from. From there type in the name of the item you would like to get.\n")
        print("When in battle, use 'attack' to attack an enemy, 'flee' to flee the battle, 'use item' to use an item.\n")

    def movement_parser(self):
        if 'north' in self.command:
            if self.player.current_room.n_to:
                self.player.current_room = self.player.current_room.n_to
            else:
                print("You have run into a dead end. Try selecting a different direction.\n")
                time.sleep(1)
            
        elif 'south' in self.command:
            if self.player.current_room.s_to:
                self.player.current_room = self.player.current_room.s_to
            else:
                print("You have run into a dead end. Try selecting a different direction.\n")
                time.sleep(1)

        elif 'east' in self.command:
            if self.player.current_room.e_to:
                self.player.current_room = self.player.current_room.e_to
            else:
                print("You have run into a dead end. Try selecting a different direction.\n")
                time.sleep(1)

        elif 'west' in self.command:
            if self.player.current_room.w_to:
                self.player.current_room = self.player.current_room.w_to
            else:
                print("You have run into a dead end. Try selecting a different direction.\n")
                time.sleep(1)

        else:
            print("Which direction would you like to move?\n")
            self.command = input("North, south, east, or west?\n").lower()
            self.movement_parser()
            
    def get_item_parser(self):
        if self.player.current_room.items:
            self.player.current_room.print_items_in_room()
            retrieved_item = input("Please type in the name of the item you would like to get.\n")
            self.retrieved_item = self.player.current_room.items[retrieved_item]
            print(f"You have picked up the {self.player.current_room.items[retrieved_item].name}\n")
            self.player.current_room.remove_item_from_room(retrieved_item)
            self.player.add_to_inventory(self.retrieved_item)
        else:
            print("There are no items available in this room.\n") # inform player there are no available items to pick up
            time.sleep(1)
        

    def check_inventory(self):
        self.player.print_inventory()

    def check_room_items(self):
        self.player.current_room.print_items_in_room()

    def use_item(self):
        if self.player.inventory:
            self.player.print_inventory()
            used_item = input("Which item would you like to use?\n")
            self.player.remove_item_from_inventory(used_item)

    def quit_game(self):
        exit()

# if __name__ == "__main__":
#     room = Room("outside", "Test", items={'torch' : Item('Torch', 'testing',), 'key' : Item("Key", "testing2")})
#     player = Player("Daniel", room)
#     while True:
#         command = InputParser(player)
#         if 'move' in command.command:
#             direction = command.movement_parser()
#             print(f"You have moved {direction}.")
#         elif 'get' in command.command:
#             command.get_item_parser()
#         elif 'help' in command.command:
#             command.help()
#         elif 'check inventory' in command.command:
#             command.check_inventory()
#         elif 'check room' in command.command or 'check items in room' in command.command or 'check room items' in command.command:
#             command.check_room_items()
#         elif 'use' in command.command or 'use item' in command.command:
#             command.use_item()
#         elif 'quit' in command.command or 'q' in command.command:
#             command.quit_game()