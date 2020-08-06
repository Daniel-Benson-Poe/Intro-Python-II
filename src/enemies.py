import random

class Enemy:
    def __init__(self, name, health=15):
        self.name = name
        self.health = health

    def roll_damage(self):
        # RNG for damage within a certain range
        return random.randint(5, 10)
    
    def take_damage(self, damage):
        # Removes damage dealt from own health
        self.health = self.health - damage

    def print_description(self):
        print(f"A nasty {self.name} stands before you, ready to attack.")