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

    # Add __str__ method for printing out location name and description
    def __str__(self):
        return f"You currently reside in the {self.name}. {self.description}"
