import random

class Battle:
    def __init__(self, player, enemy, first=None, second=None, participant_turn=None):
        self.player = player  # call player participating in battle
        self.enemy = enemy  # call enemy participating in battle
        self.first = first  # first to act in battle
        self.second = second  # second to act in battle
        self.participant_turn = participant_turn  # Keep track of turn cycle
    
    def determine_turn_cycle(self):
        choices = [self.player, self.enemy]  # create list of choices that includes player and enemy
        first = random.choice(choices)  # randomly select player or enemy as getting first action
        choices.remove(first)  # remove who was already selected from the list
        second = choices[0]  # select remaining player or enemy as getting second action
        self.first = first
        self.second = second
        self.participant_turn = self.first

    def attack_sequence(self):
        return self.participant_turn.roll_damage()

    def take_damage(self, dmg):
        return self.second.take_damage(dmg)

    def end_turn(self):
        temp_first_storage = self.first
        self.first = self.second
        self.second = temp_first_storage