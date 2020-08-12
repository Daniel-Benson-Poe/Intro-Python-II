class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Cave(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class City(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Town(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Dungeon(Location):
    def __init__(self, name, description):
        super().__init__(name, description)

class Forest(Location):
    def __init__(self, name, description):
        super().__init__(name, description)