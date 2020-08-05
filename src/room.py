# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    # parameters should include name, description, n_to, s_to, e_to, w_to
    # the directional parameters should default to None and be overridden depending on each room
    def __init__(self, name=None, description=None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

######
## Easier way to do this may be to have only a Room class and create each room
## in the adv.py file. Commit this version of room.py then we will work on the
## new version.
######


class Outside(Room):

    def __init__(self, name=None, description=None, n_to=None):

        # Create outside room that inherits from the Room class
        # Inherit from Room
        super(Outside, self).__init__(name, description, n_to)
        # set n_to to foyer room
        self.n_to = Foyer()
        # set name to "Outside Cave Entrance"
        self.name = "Outside Cave Entrance"
        # set description
        self.description = "North of you, the cave mount beckons."

    # Create __str__ method to print name and description
    def __str__(self):
        return f"""
        You currently reside in the {self.name}.
        {self.description}
        """


class Foyer(Room):

    def __init__(self, name=None, description=None, n_to=None, s_to=None, e_to=None):

        # Create foyer room that inherits from Room class
        # Inherit from Room
        super(Foyer, self).__init__(name, description, s_to, n_to, e_to)
        # set s_to to outside room
        self.s_to = Outside()
        # set n_to to overlook room
        self.n_to = Overlook()
        # set e_to to narrow room
        self.e_to = Narrow()
        # set name to "Foyer"
        self.name = "Foyer"
        # set description
        self.Description = """Dim light filters in from the south. Dusty
                           passages run north and east."""
    # Create __str__ method to print name and description
    def __str__(self):
        return f"""
        You currently reside in the {self.name}.
        {self.description}
        """


class Overlook(Room):
    def __init__(self, name=None, description=None, s_to=None):

        # Create overlook room that inherits from Room class
        # inherit from room class
        super(Overlook, self).__init__(name, description, s_to)
        # set s_to to foyer room
        self.s_to = Foyer()
        # set name to "Grand Overlook"
        self.name = "Grand Overlook"
        # set description
        self.description = """A steep cliff appears before you, falling
                           into the darkness. Ahead to the north, a light flickers in
                           the distance, but there is no way across the chasm."""
    # Create __str__ method to print name and description
    def __str__(self):
        return f"""
        You currently reside in the {self.name}.
        {self.description}
        """


class Narrow(Room):
    def __init__(self, name=None, description=None, n_to=None, w_to=None):
        # create narrow room that inherits from Room class
        # inherit from Room class
        super(Narrow, self).__init__(name, description, w_to, n_to)
        # set w_to to foyer
        self.w_to = Foyer()
        # set n_to to treasure room
        self.n_to = Treasure()
        # set name to "Narrow Passage"
        self.name = "Narrow Passage"
        # set description
        self.description = """The narrow passage bends here from west
                           to north. The smell of gold permeates the air."""
    # Create __str__ method to print name and description
    def __str__(self):
        return f"""
        You currently reside in the {self.name}.
        {self.description}
        """


class Treasure(Room):
    def __init__(self, name=None, description=None, s_to=None):
        # Create treasure room that inherits from Room class
        # inherit from Room class
        super(Treasure, self).__init__(name, description, s_to)
        # set s_to to Narrow
        self.s_to = Narrow()
        # set name to "Treasure Room"
        self.name = "Treasure Room"
        # set description
        self.description = """You've found the long-lost treasure
                           chamber! Sadly, it has already been completely emptied by
                           earlier adventurers. The only exit is to the south."""
    # Create __str__ method to print name and description
    def __str__(self):
        return f"""
        You currently reside in the {self.name}.
        {self.description}
        """

if __name__ == "__main__":
    # Test that the classes work.
    outside = Outside()
    print(outside.__str__)
    print(outside.n_to.name)
    foyer = Foyer()
    print(foyer.n_to.name)
    print(foyer.s_to.name)
    print(foyer.e_to.name)
    print(foyer.__str__)
    overlook = Overlook()
    print(overlook.s_to.name)
    print(overlook.__str__)
    narrow = Narrow()
    print(narrow.n_to.name)
    print(narrow.w_to.name)
    print(narrow.__str__)
    treasure = Treasure()
    print(treasure.s_to.name)
    print(treasure.__str__)