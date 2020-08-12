from items import Item
# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # parameters should include name, description, n_to, s_to, e_to, w_to
    # the directional parameters should default to None and be overridden depending on each room
    def __init__(self, name, description, n_to=None, s_to=None, 
                 e_to=None, w_to=None, items={}, items_useable={},
                 enemy=None):
        self.name = name  # room name
        self.description = description  # room description
        self.n_to = n_to  # room connected to the north
        self.s_to = s_to  # room connected to the south
        self.e_to = e_to  # room connected to the east
        self.w_to = w_to  # room connected to the west
        self.items = items  # items that can be found in the room
        self.items_useable = items_useable  # items that can be used in this room
        self.enemy = enemy  # Enemies found within the room

    # Add __str__ method for printing out location name and description
    def print_room_details(self):
         print(f"You currently reside in the {self.name}. {self.description}")

    def remove_item_from_room(self, item):
        self.items.pop(item)

    def print_items_in_room(self):
        print(f"The room contains the following item/s: {[(i.name, i.description) for i in self.items.values()]}\n")

# Testing purposes
if __name__ == "__main__":
    room = Room("outside", "Test", items={'torch' : Item('Torch', 'testing',), 'key' : Item("Key", "testing2")})
    room.print_items_in_room()