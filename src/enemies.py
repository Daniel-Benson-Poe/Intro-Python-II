import random

class Enemy:
    def __init__(self, name, health=15):
        self.name = name
        self.health = health

    def roll_damage(self, weapon_dmg_range):
        # RNG for damage within a certain range
        return random.randint(weapon_dmg_range[0], weapon_dmg_range[1])
        
    def take_damage(self, damage):
        # Removes damage dealt from own health
        self.health = self.health - damage

    def print_description(self):
        print(f"A nasty {self.name} stands before you, ready to attack.")

    def print_attack(self):
        print(f"The {self.name} swings at you with its razor sharp claws.")