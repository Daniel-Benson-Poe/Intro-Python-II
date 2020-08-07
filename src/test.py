from room import Room
from player import Player
from items import Item
import time
from enemies import Enemy
from battle_sequence import Battle

items = {'dagger' : Item("Basic Dagger", "Just a basic dagger. Can be used to cause minimal damage. 10-15 dmg dealt.")}

room = Room("Practice Room", """This room is a practice room, its contents being a mobile wooden dummy and the player. 
                            its purpose is to test out the battle_sequence function.""")
enemy = Enemy("Wooden Dummy")
player = Player("Player Dummy", room, inventory=[items['dagger']])

# print(enemy.name)
# print(enemy.health)
# print(player.name)
# print(player.health)
# player.print_inventory()

test_battle = Battle(player, enemy)

test_battle.determine_turn_cycle()
print(f"Turn order: First action: {test_battle.first.name}, Second action: {test_battle.second.name}")

while player.health > 0 and enemy.health > 0:
    if test_battle.first == player:
        print("Input your action: \n")
        action = input("'a' (to attack), 'f' (flee)\n")

        if action == 'a':
            dmg_dealt = test_battle.attack_sequence(weapon_dmg_range=[10, 15])
            test_battle.take_damage(dmg_dealt)
            print(f"{player.name} deals {dmg_dealt} damage to {enemy.name}.")
            if enemy.health < 0:
                print(f"{enemy.name} has 0 hit points left.")
            else:    
                print(f"{enemy.name} has {enemy.health} hit points left.")
            test_battle.end_turn()

        if action == 'f':
            print("You have fled from battle.")
            exit()

    else:
        dmg_dealt = test_battle.attack_sequence()
        test_battle.take_damage(dmg_dealt)
        print(f"{enemy.name} deals {dmg_dealt} damage to {player.name}.")
        print(f"{player.name} has {player.health} hit points left.")
        test_battle.end_turn()

test_battle.end_battle_sequence(player, enemy)