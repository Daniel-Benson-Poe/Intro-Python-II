# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # parameters should include name, description, n_to, s_to, e_to, w_to
    # the directional parameters should default to None and be overridden depending on each room
    def __init__(self, name, description, n_to=None, s_to=None, 
                 e_to=None, w_to=None, items=[], items_useable=[],
                 enemies=None):
        self.name = name  # room name
        self.description = description  # room description
        self.n_to = n_to  # room connected to the north
        self.s_to = s_to  # room connected to the south
        self.e_to = e_to  # room connected to the east
        self.w_to = w_to  # room connected to the west
        self.items = items  # items that can be found in the room
        self.items_useable = items_useable  # items that can be used in this room
        self.enemies = enemies  # Enemies found within the room

    # Add __str__ method for printing out location name and description
    def __str__(self):
        return f"You currently reside in the {self.name}. {self.description}"

    def remove_item_from_room(self, item):
        self.items.remove(item)

    def print_items_in_room(self):
        print(f"The room contains the following item/s: {[i.name for i in self.items]}\n")
