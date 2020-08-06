# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    # set a default for name and current_room? player should always start outside
    def __init__(self, name, current_room, inventory=[], health=20):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.health = health
    
    # print out player movement.
    def __str__(self):
        return f"You have entered the {self.current_room.name}.\n"

    def add_to_inventory(self, item):
        # add item to inventory
        self.inventory.append(item)
        self.print_inventory()

    def remove_item_from_inventory(self, item):
        self.inventory.remove(item)

    def print_inventory(self):
        print("Your inventory contains: ", [f"{item.name}, {item.description}" for item in self.inventory],'\n')

    def roll_damage(self, weapon_dmg_range=[5, 10]):
        # RNG for damage within a certain range
        return random.randint(weapon_range[0], weapon_range[1])
    
    def take_damage(self, damage):
        # Removes damage dealt from own health
        self.health = self.health - damage