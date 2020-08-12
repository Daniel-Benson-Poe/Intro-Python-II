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

test_battle.main_battle_loop()