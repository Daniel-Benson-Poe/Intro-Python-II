import random
from items import Item, Weapon

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    # set a default for name and current_room? player should always start outside
    def __init__(self, current_room=None, inventory={}, 
                equipped_weapon=Weapon('Fists', "Ye ol' left jab, right hook", [5, 10]), health=20):
        self.name = None
        self.gender = None
        self.race = None
        self.current_room = current_room
        self.inventory = inventory
        self.equipped_weapon = equipped_weapon
        self.health = health
        self.last_action = None
        self.used_item = None

        # Run below methods to set up character
        self.select_name()
        self.select_race()
        self.select_gender()

    def select_race(self):
        print("What is your character's race?")
        print("Select a number from the following list: \n")
        print("1. Human\n2. Elf\n3. Dwarf\n")
        race_selection = int(input())
        if race_selection == 1:
            self.race = "Human"
        elif race_selection == 2:
            self.race = "Elf"
        elif race_selection == 3:
            self.race = "Dwarf"
        else:
            print("I'm sorry, that is not a viable option. Please try again.")
            self.select_race()

    def select_gender(self):
        print("What is your character's gender?")
        print("Please select a number from the following list. \n")
        print("1. Male\n2. Female\n")
        gender_selection = int(input())
        if gender_selection == 1:
            self.gender = "Male"
        elif gender_selection == 2:
            self.gender = "Female"
        else:
            print("I'm sorry, that is not a viable option. Please try again.")
            self.select_gender()

    def select_name(self):
        print("What is your character's name?")
        self.name = input()
    
    # print out player movement.
    def __str__(self):
        return f"You have entered the {self.current_room.name}.\n"

    def add_to_inventory(self, item):
        # add item to inventory
        self.inventory[item.name.lower()] = item
        self.print_inventory()
        self.last_action = "Add to inventory"

    def remove_item_from_inventory(self, item):
        self.used_item = item.lower()
        del self.inventory[item]
        self.last_action = "Used item"

    def print_inventory(self):
        print("Your inventory contains: ", [f"{item.name}, {item.description}" for item in self.inventory.values()],'\n')
        self.last_action = "Print inventory"

    def roll_damage(self):
        weapon_dmg_range = self.equipped_weapon.dmg_range
        # RNG for damage within a certain range
        return random.randint(weapon_dmg_range[0], weapon_dmg_range[1])
    
    def take_damage(self, damage):
        # Removes damage dealt from own health
        self.health = self.health - damage
