# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # parameters should include name, description, n_to, s_to, e_to, w_to
    # the directional parameters should default to None and be overridden depending on each room
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

class Outside(Room):
    # Create outside room that inherits from the Room class
    # TODO: n_to should be set to foyer
    # TODO: name should be set to "Outside Cave Entrance"
    # TODO: Description should also be set
    # TODO: Create __str__ method for description
    pass

class Foyer(Room):
    # Create foyer room that inherits from Room class
    # TODO: s_to should be set to outside
    # TODO: n_to should be set to overlook
    # TODO: e_to should be set to narrow
    # TODO: name should be set to "Foyer"
    # TODO: Description should be set
    # TODO: create __str__ method for description
    pass

class Overlook(Room):
    # Create overlook room that inherits from Room class
    # TODO: s_to should be set to foyer
    # TODO: name should be set to "Grand Overlook"
    # TODO: description should be set
    # TODO: create __str__ method for description
    pass

class Narrow(Room):
    # create narrow room that inherits from Room class
    # TODO: w_to should be set to foyer
    # TODO: n_to should be set to treasure
    # TODO: name should be set to "Narrow Passage"
    # TODO: description should be set
    # TODO: create __str__ method for description
    pass

class Treasure(Room):
    # Create treasure room that inherits from Room class
    # TODO: s_to should be set to narrow
    # TODO: name should be set to "Treasure Room"
    # TODO: description should be set
    # TODO: create __str__ method for description
    pass
