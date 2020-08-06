# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    # set a default for name and current_room? player should always start outside
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    
    # print out player movement.
    def __str__(self):
        return f"You have entered the {self.current_room.name}."

    def add_to_inventory(self, item):
        # add item to inventory
        self.inventory.append(item)
        self.print_inventory()

    def remove_item_from_inventory(self, item):
        self.inventory.remove(item)

    def print_inventory(self):
        print("Your inventory contains: ", [f"{item.name}, {item.description}" for item in self.inventory],'\n')