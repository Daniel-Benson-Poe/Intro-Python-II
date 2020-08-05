# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    # set a default for name and current_room? player should always start outside
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    # TODO: create __str__ method to print out player movement.
    def __str__(self):
        return f"You have entered the {self.current_room.name}."